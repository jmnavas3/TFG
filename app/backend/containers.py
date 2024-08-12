from injector import Module, Binder, singleton

from app.backend.src.alerts.application.query.get_alerts_query import GetAlertsQuery
from app.backend.src.alerts.infrastructure.repository.alert_repository import AlertRepository
from app.backend.src.alerts.infrastructure.services.import_csv_service import CambioArchivoHandler
from app.backend.database.database import Database
from app.backend.src.rules.application.command.enable_disable_rule_handler import EnableDisableRuleHandler
from app.backend.src.rules.application.query.get_rules_query import GetRulesQuery
from app.backend.src.rules.domain.services.enable_disable_rule_service import EnableDisableRuleService
from app.backend.src.rules.infrastructure.repository.rules_repository import RulesRepository
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
        rules_repo = self.configure_rules_repo(db)

        csv_path = ''
        file_path = ''

        "Alert Items"
        alert_handler = CambioArchivoHandler(repository=alert_repo,
                                             csv=csv_path,
                                             file_path=file_path)
        get_alerts_query = GetAlertsQuery(repository=alert_repo)

        "Rule Items"
        enable_disable_rule_service = EnableDisableRuleService(repository=rules_repo, script=EnableDisableRuleScript())
        enable_disable_rule_handler = EnableDisableRuleHandler(service=enable_disable_rule_service)

        get_rules_query = GetRulesQuery(repository=rules_repo)

        "Bindings"
        binder.bind(CambioArchivoHandler, to=alert_handler, scope=singleton)
        binder.bind(EnableDisableRuleService, to=enable_disable_rule_service, scope=singleton)
        binder.bind(EnableDisableRuleHandler, to=enable_disable_rule_handler, scope=singleton)
        binder.bind(GetRulesQuery, to=get_rules_query, scope=singleton)
        binder.bind(GetAlertsQuery, to=get_alerts_query, scope=singleton)

    def configure_alert_repo(self, db: Database) -> AlertRepository:
        alert_repository = AlertRepository(Database.session_factory(db=db))
        return alert_repository

    def configure_rules_repo(self, db: Database) -> RulesRepository:
        rules_repository = RulesRepository(Database.session_factory(db=db))
        return rules_repository
