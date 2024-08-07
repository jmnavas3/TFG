import logging
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

# repository imports
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session

from app.backend.configuration.configuration import Config
from app.backend.database.models.fast import Fast as EntityModel


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


class AlertRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self._session_factory = session_factory
        self._engine = create_engine(Config.create('/config/config.yml').__dict__["SQLALCHEMY_DATABASE_URI"])
    
    def save(self, line="", csv=''):
        # data frame de pandas
        df = pd.read_csv(csv)
        df.to_sql(EntityModel.__tablename__, self._engine, if_exists='replace')
        # with self._session_factory() as session:
        #     try:
        #         df.to_sql(EntityModel.__tablename__, session.connection(), if_exists='append', index=False)
        #         return True
        #     except Exception as e:
        #         print(e)
        # with open(self._file_path, 'r') as file:
        #     reader = csv.reader(f)
        #     columns = next(reader)
        #     query = 'insert into MyTable({0}) values ({1})'
        #     query = query.format(','.join(columns), ','.join('?' * len(columns)))
        #     cursor = connection.cursor()
        #     for data in reader:
        #         alert = get_entity(data)
        #         session.add(alert)
        #     cursor.commit()


# configuramos logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# obtenemos ruta al directorio app
# path_root = str(Path(__file__).parents[5])
# file_path = f'{path_root}/suricata/log/fast.log'
# csv_path = f'{path_root}/suricata/log/fast.csv'

# event_handler = CambioArchivoHandler()
# observer = Observer()
# observer.schedule(event_handler, path=self._file_path, recursive=False)
# observer.start()

# event_handler = CambioArchivoLine(csv=csv_path)
# observer = Observer()
# observer.schedule(event_handler, path=file_path, recursive=False)
# observer.start()

# logging_event_handler = LoggingEventHandler()
# observer_out = Observer()
# observer_out.schedule(logging_event_handler, path=file_path, recursive=False)
# observer_out.start()

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
    # observer.stop()
    # observer_out.stop()
# observer.join()
# observer_out.join()
