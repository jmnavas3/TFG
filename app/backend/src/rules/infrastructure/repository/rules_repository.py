from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session

from app.backend.database.models.ids_rules import IdsRules as EntityModel
from app.backend.src.base.infrastructure.repository.base_repository import BaseRepository


class RulesRepository(BaseRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    @staticmethod
    def map_entity(model: EntityModel) -> dict:
        estado = "activada"
        if not model.active:
            estado = "deshabilitada"
        return {
            "id": model.sid,
            "regla": model.rule,
            "actualizaciones": model.rev,
            "descripcion": model.msg,
            "estado": estado
        }

    def get_rules(self, page: int = 0):
        with self.session_factory() as session:
            try:
                query = session.query(EntityModel)
                data = self.paginate_query(query, page).all()
                if not data and page == 0:
                    return []
                return [self.map_entity(x) for x in data]
            except Exception as e:
                print(self.error_message(e))
                raise Exception(e)
