import time

from app.backend.src.alerts.domain.contracts.import_csv_contract import ImportCsv
from app.backend.src.alerts.domain.contracts.file_handler_contract import FileHandler


class AlertsCsvFileEventHandler(FileHandler):
    modified = 0

    def __init__(self, service: ImportCsv, file_path: str = ""):
        self.service = service
        self._file_path = file_path

    def on_file_modified(self, event):
        try:
            self.modified = (self.modified + 1) % 2
            if event.src_path == self._file_path and self.modified == 1:
                # esperamos a que termine de modificarse el archivo
                time.sleep(3)
                print(f"{self._file_path} ha sido modificado")
                self.service.import_csv()
        except Exception as e:
            print(e)

    def on_file_created(self, event):
        pass
