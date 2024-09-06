from collections import Counter
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

from app.backend.database.models.fast import Fast as EntityModel
from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.base.infrastructure.middleware.mikrotik_middleware import MikrotikConnector
from app.backend.src.base.infrastructure.repository.base_repository import BaseRepository


class AlertRepository(BaseRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory
        self.router_conn = MikrotikConnector()
        self.high_severity_alerts = ["DDoS", "SQL", "Injection", "Trojan", "Denial", "GPL ATTACK", "PyCurl"]
        self.private_ranges = ["192.168.", "10.", "172."]

    @staticmethod
    def map_entity(model: EntityModel) -> dict:
        return {
            "fecha": model.fecha,
            "prioridad": model.prioridad,
            "protocolo": model.protocolo,
            "ip_origen": model.ip_origen,
            "puerto_origen": model.puerto_origen,
            "ip_destino": model.ip_destino,
            "puerto_destino": model.puerto_destino,
            "identificador": model.identificador,
            "alerta": model.alerta,
            "clasificacion": model.clasificacion,
            "reciente": "nueva" if model.reciente else "antigua",
        }

    def get_alert_by_id(self, alert_id: int):
        with self.session_factory() as session:
            alert = session.query(EntityModel).filter(EntityModel.id == alert_id).first()
            if alert is None:
                return None

            return self.map_entity(alert)

    def get_alerts(self, request: OrderPagination):
        with self.session_factory() as session:
            try:
                query = session.query(EntityModel)
                if request.field:
                    query = self.apply_order(query, request.field, request.sort_type, EntityModel)
                data = self.paginate_query(query, request.page, request.per_page).all()
                if not data and request.page == 0:
                    return []
                values = [self.map_entity(x) for x in data]
                total = self.get_total(query)
                return {"data": values, "total": total, **request.as_dict()}
            except Exception as e:
                print(self.error_message(e))
                raise Exception(e)

    def update_old(self):
        with self.session_factory() as session:
            try:
                query = update(EntityModel) \
                    .where(EntityModel.reciente == True) \
                    .values(reciente=False)
                session.execute(query)
                session.commit()
            except Exception as e:
                print(self.error_message(e))
                raise Exception(e)

    def analyze(self):
        with self.session_factory() as session:
            try:
                suspicious_ip_list = []
                ip_counter = Counter()
                # queries para obtener alertas
                query = session.query(EntityModel.ip_destino).filter(EntityModel.reciente == True).all()

                # count all the ip addresses repeated
                for ip in query:
                    ip_counter[ip] += 1

                for ip, counter in ip_counter.items():
                    if counter > 1:
                        suspicious_ip_list.append(ip)

                return query
            except Exception as e:
                print(self.error_message(e))
                raise Exception(e)

    def get_priority_alerts(self):
        with self.session_factory() as session:
            return session.query(EntityModel.ip_origen, EntityModel.ip_destino).filter(
                EntityModel.reciente == True,
                EntityModel.prioridad == 1).all()

    def get_message_alerts(self):
        message_alerts = []
        with self.session_factory() as session:
            query = session.query(EntityModel.ip_origen, EntityModel.ip_destino, EntityModel.alerta).filter(
                    EntityModel.reciente == True,
                    EntityModel.prioridad != 1).all()

            for alerta in query:
                for high_alert in self.high_severity_alerts:
                    if high_alert in alerta.alerta:
                        message_alerts.append(alerta)

            # for high_alert in self.high_severity_alerts:
            #     alert_list = session.query(EntityModel.ip_origen, EntityModel.ip_destino).filter(
            #         EntityModel.reciente == True,
            #         EntityModel.prioridad != 1,
            #         EntityModel.alerta.contains(high_alert)).all()
            #     if alert_list:
            #         message_alerts.append(alert_list)
            return message_alerts

    def drop_dangerous_alerts(self):
        try:
            # query to get new alerts' ip addresses with high priority
            priority_query = self.get_priority_alerts()
            # query to get new alerts' ip addresses with any critical message
            message_query = self.get_message_alerts()

            priority_blacklist = set(self.get_public_ip(alert.ip_origen, alert.ip_destino) for alert in priority_query)
            messages_blacklist = set(self.get_public_ip(alert.ip_origen, alert.ip_destino) for alert in message_query)
            priority_blacklist.update(messages_blacklist)

            self.router_conn.add_to_blacklist(priority_blacklist)
            return priority_blacklist
        except Exception as e:
            # print(self.error_message(e))
            raise Exception(e)

    def is_public(self, ip_address: str):
        """return false if an ip address is in the private ip addresses' range"""

        is_public = True
        for ip_range in self.private_ranges:
            if ip_range in ip_address:
                is_public = False
                break

        return is_public

    def get_public_ip(self, ip_origen, ip_destino):
        public_ip = ip_origen if self.is_public(ip_origen) else ip_destino
        # if not self.is_public(ip_destino): check port service

        return public_ip
