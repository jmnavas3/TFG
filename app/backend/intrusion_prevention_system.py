import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from app.backend.src.alerts.infrastructure.repository.alert_repository import AlertRepository

from app.backend.src.base.infrastructure.adapters.watchdog_adapter import WatchdogAdapter
from app.backend.src.alerts.application.event_handlers.alerts_event_handler import AlertsEventHandler
from app.backend.src.alerts.infrastructure.services.import_alerts_service import ImportAlertsService

from app.backend.database.database import Database
from app.backend.configuration.configuration import Config


def run_intrusion_prevention_system():
    repo = AlertRepository(Database.session_factory(db=db))
    service = ImportAlertsService(engine=db.get_engine(), csv=config["CSV_ALERTS"])
    event_handler = AlertsEventHandler(service, repo, config["CSV_ALERTS"])
    observer = WatchdogAdapter(event_handler, config["CSV_ALERTS"])
    observer.start()


if __name__ == '__main__':
    config = Config.create("/config/config.yml").__dict__
    db = Database(config['SQLALCHEMY_DATABASE_URI'])
    run_intrusion_prevention_system()

