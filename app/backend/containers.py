from injector import Module, Binder, singleton
from backend.src.alerts.infrastructure.services.import_csv_service import AlertRepository, CambioArchivoHandler
from backend.database.database import Database


class Container(Module):
    def __init__(self, database_connection: str = ''):
        self._database_connection = database_connection

    def configure_db(self):
        db = Database(self._database_connection)
        return db

    def configure(self, binder: Binder) -> None:
        db = self.configure_db()
        binder.bind(Database, to=db, scope=singleton)

        alert_repo = self.configure_alert_repo(db)

        "Items"
        alert_handler = CambioArchivoHandler(repository=alert_repo)
        
        "Bindings"
        binder.bind(CambioArchivoHandler, to=alert_handler, scope=singleton)


    def configure_alert_repo(self, db: Database) -> AlertRepository:
        alert_repository = AlertRepository(Database.session_factory(db=db))
        return alert_repository
