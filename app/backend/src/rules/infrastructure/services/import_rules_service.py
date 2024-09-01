from sqlalchemy import Engine

from app.backend.database.models.ids_rules import IdsRules as EntityModel
from app.backend.src.base.infrastructure.adapters.pandas_adapter import PandasAdapter


class ImportRulesService(PandasAdapter):
    _entity_model = EntityModel.__tablename__

    def __init__(self, engine: Engine, csv: str = ""):
        # <column_name, sqlalchemy_type> dict to store csv with correct data types of columns using pandas
        dtypes: dict = {k: getattr(EntityModel, k).type for k in EntityModel.__table__.columns.keys()}
        super().__init__(engine, csv, self._entity_model, dtypes)
