from injector import Binder, singleton

from app.backend.configuration.configuration import Config
from app.backend.src.base.infrastructure.container.base_container import BaseContainer
from app.backend.database.database import Database
from app.backend.src.rules.application.command.add_rule_file_handler import AddRuleFileHandler
from app.backend.src.rules.application.command.enable_disable_rule_handler import EnableDisableRuleHandler
from app.backend.src.rules.application.query.get_rules_query import GetRulesQuery
from app.backend.src.rules.domain.services.add_rule_file_service import AddRuleFileService
from app.backend.src.rules.domain.services.enable_disable_rule_service import EnableDisableRuleService
from app.backend.src.rules.infrastructure.repository.rules_repository import RulesRepository
from app.backend.src.rules.infrastructure.scripts.add_rule_file_script import AddRuleFileScript
from app.backend.src.rules.infrastructure.scripts.convert_rule_to_csv_script import ConvertRuleToCsvScript
from app.backend.src.rules.infrastructure.scripts.enable_disable_rule_script import EnableDisableRuleScript
from app.backend.src.rules.infrastructure.services.import_rules_service import ImportRulesService


class RulesContainer(BaseContainer):

    def configure(self, binder: Binder) -> None:
        db = self.configure_db()
        binder.bind(Database, to=db, scope=singleton)

        rules_repo = self.configure_rules_repo(db)
        rules_import_service = self.configure_import_service(db)

        "Rule Items"
        add_rule_file_service = AddRuleFileService(repository=rules_import_service,
                                                   csv_script=ConvertRuleToCsvScript(),
                                                   copy_script=AddRuleFileScript())
        add_rule_file_handler = AddRuleFileHandler(add_rule_file_service=add_rule_file_service)

        enable_disable_rule_service = EnableDisableRuleService(repository=rules_repo, script=EnableDisableRuleScript())
        enable_disable_rule_handler = EnableDisableRuleHandler(service=enable_disable_rule_service)

        get_rules_query = GetRulesQuery(repository=rules_repo)

        "Bindings"
        binder.bind(AddRuleFileService, to=add_rule_file_service, scope=singleton)
        binder.bind(AddRuleFileHandler, to=add_rule_file_handler, scope=singleton)
        binder.bind(EnableDisableRuleService, to=enable_disable_rule_service, scope=singleton)
        binder.bind(EnableDisableRuleHandler, to=enable_disable_rule_handler, scope=singleton)
        binder.bind(GetRulesQuery, to=get_rules_query, scope=singleton)

    def configure_rules_repo(self, db: Database) -> RulesRepository:
        rules_repository = RulesRepository(Database.session_factory(db=db))
        return rules_repository

    def configure_import_service(self, db: Database):
        rules_import_service = ImportRulesService(engine=db.get_engine(), csv=self._csv_file)
        return rules_import_service
