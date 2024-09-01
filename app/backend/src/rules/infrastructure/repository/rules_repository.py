from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import update
from sqlalchemy.orm import Session

from app.backend.database.models.ids_rules import IdsRules as EntityModel
from app.backend.src.base.application.dto.pagination import OrderPagination
from app.backend.src.base.infrastructure.repository.base_repository import BaseRepository


class RulesRepository(BaseRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    @staticmethod
    def map_entity(model: EntityModel) -> dict:
        estado = "activada"
        if not model.active:
            estado = "desactivada"
        return {
            "id": str(model.sid),
            "regla": model.rule,
            "actualizaciones": model.rev,
            "descripcion": model.msg,
            "estado": estado
        }

    def get_rule_by_sid(self, rule_sid: str):
        with self.session_factory() as session:
            rule = session.query(EntityModel).filter(EntityModel.sid == int(rule_sid)).first()
            if rule is None:
                return None

            return self.map_entity(rule)

    def rule_exists(self, rule_sid: str):
        if self.get_rule_by_sid(rule_sid):
            return True
        return False

    def get_rules(self, request: OrderPagination):
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

    def update_status(self, sid: str, action: bool):
        with self.session_factory() as session:
            try:
                query = update(EntityModel).where(EntityModel.sid == int(sid)).values(active=action)
                session.execute(query)
                session.commit()
                return True
            except Exception as e:
                print(self.error_message(e))
                return False
