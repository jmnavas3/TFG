from contextlib import AbstractContextManager
from typing import Callable

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.backend.configuration.configuration import Config
from app.backend.database.models.fast import Fast as EntityModel
from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.base.infrastructure.repository.base_repository import BaseRepository


class AlertRepository(BaseRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory
        self._engine = create_engine(Config.create('/config/config.yml').__dict__["SQLALCHEMY_DATABASE_URI"])

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
        }

    def save(self, csv=''):
        dataframe = pd.read_csv(csv)
        dataframe.to_sql(EntityModel.__tablename__, self._engine, if_exists='append', index=False)

    def get_alerts(self, request: OrderPagination):
        with self.session_factory() as session:
            try:
                query = session.query(EntityModel)
                if request.field is not None:
                    query = self.apply_order(query, request.field, request.sort_type, EntityModel)
                data = self.paginate_query(query, request.page, request.per_page).all()
                if not data and request.page == 0:
                    return []
                return [self.map_entity(x) for x in data]
            except Exception as e:
                print(self.error_message(e))
                raise Exception(e)

