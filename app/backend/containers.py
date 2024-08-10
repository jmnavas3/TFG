from injector import Module, Binder, singleton
from app.backend.src.alerts.infrastructure.services.import_csv_service import AlertRepository, CambioArchivoHandler
from app.backend.database.database import Database
from app.backend.src.rules.application.command.enable_disable_rule_handler import EnableDisableRuleHandler
from app.backend.src.rules.domain.services.enable_disable_rule_service import EnableDisableRuleService
from app.backend.src.rules.infrastructure.scripts.enable_disable_rule_script import EnableDisableRuleScript


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

        csv_path = ''
        file_path = ''

        "Items"
        alert_handler = CambioArchivoHandler(repository=alert_repo,
                                             csv=csv_path,
                                             file_path=file_path)

        enable_disable_rule_service = EnableDisableRuleService(repository=alert_repo, script=EnableDisableRuleScript())
        enable_disable_rule_handler = EnableDisableRuleHandler(service=enable_disable_rule_service)

        "Bindings"
        binder.bind(CambioArchivoHandler, to=alert_handler, scope=singleton)
        binder.bind(EnableDisableRuleService, to=enable_disable_rule_service, scope=singleton)
        binder.bind(EnableDisableRuleHandler, to=enable_disable_rule_handler, scope=singleton)


    def configure_alert_repo(self, db: Database) -> AlertRepository:
        alert_repository = AlertRepository(Database.session_factory(db=db))
        return alert_repository
