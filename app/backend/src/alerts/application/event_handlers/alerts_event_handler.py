import time

from app.backend.src.base.domain.contracts.import_csv_contract import ImportCsv
from app.backend.src.alerts.domain.contracts.file_handler_contract import FileHandler


class AlertsEventHandler(FileHandler):
    """Life cycle class for alerts. From the alerts' file modified event to the firewall rule creation"""

    modified = 0

    def __init__(self, service: ImportCsv, repo, file_path: str = ""):
        self.service = service
        self._file_path = file_path
        self.repo = repo

    def execute_alerts_cycle(self):
        # update lasts alerts' state to old
        self.repo.update_old()

        # import new alerts
        self.service.import_csv()

        # create rules for high severity & dangerous messages alerts
        addresses_dropped = self.repo.drop_dangerous_alerts()
        print(addresses_dropped)

    def on_file_modified(self, event):
        try:
            # this method is called 2 times by modification, we only need to execute the life cycle one.
            self.modified = (self.modified + 1) % 2
            if event.src_path == self._file_path and self.modified == 1:
                time.sleep(3)
                self.execute_alerts_cycle()
        except Exception as e:
            print(e)

    def on_file_created(self, event):
        pass
