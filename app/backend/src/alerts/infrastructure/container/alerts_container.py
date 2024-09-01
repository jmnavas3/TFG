from injector import Binder, singleton

from app.backend.src.base.infrastructure.container.base_container import BaseContainer
from app.backend.database.database import Database
from app.backend.src.alerts.application.query.get_alerts_query import GetAlertsQuery
from app.backend.src.alerts.infrastructure.repository.alert_repository import AlertRepository


class AlertsContainer(BaseContainer):
    def configure(self, binder: Binder) -> None:
        db = self.configure_db()
        binder.bind(Database, to=db, scope=singleton)

        alert_repo = self.configure_alert_repo(db)

        "Alert Items"
        get_alerts_query = GetAlertsQuery(repository=alert_repo)

        "Bindings"
        binder.bind(GetAlertsQuery, to=get_alerts_query, scope=singleton)

    def configure_alert_repo(self, db: Database) -> AlertRepository:
        alert_repository = AlertRepository(Database.session_factory(db=db))
        return alert_repository
