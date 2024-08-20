from sqlalchemy import Engine

from app.backend.database.models.fast import Fast as EntityModel
from app.backend.src.alerts.domain.contracts.import_csv_contract import ImportCsv
from app.backend.src.base.infrastructure.adapters.pandas_adapter import PandasAdapter


class ImportCsvService(ImportCsv):
    _entity_model = EntityModel.__tablename__

    def __init__(self, engine: Engine, csv: str = ""):
        self._adapter = PandasAdapter(engine, csv, self._entity_model)

    def import_csv(self):
        try:
            self._adapter.import_csv()
        except Exception as e:
            print(str(e))
