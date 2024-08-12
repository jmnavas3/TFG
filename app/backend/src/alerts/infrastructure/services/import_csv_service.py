import time

from watchdog.events import FileSystemEventHandler, LoggingEventHandler


class CambioArchivoLine(FileSystemEventHandler):
    def __init__(self, log: str = "", csv: str = ""):
        self._csv = csv
        self._file_path = log

    def on_modified(self, event):
        if event.src_path == self._file_path:
            time.sleep(1)
            print("comprobando")
            with open(self._csv, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())


class CambioArchivoHandler(FileSystemEventHandler):
    _modified = 0

    def __init__(self, repository, csv: str = "", file_path: str = ""):
        self._repository = repository
        self._csv = csv
        self._file_path = file_path

    def on_modified(self, event):
        self._modified = (self._modified + 1) % 2
        if event.src_path == self._file_path and self._modified == 1:
            # esperamos a que termine de modificarse el archivo
            time.sleep(2)
            print(f"{self._file_path} ha sido modificado")
            self.import_csv()

    def import_csv(self):
        print("Importando CSV a DB...")
        self._repository.save(csv=self._csv)
