from injector import Module

from app.backend.database.database import Database


class BaseContainer(Module):
    def __init__(self, database_connection: str = '', csv_file: str = ""):
        self._database_connection = database_connection
        self._csv_file = csv_file

    def configure_db(self):
        db = Database(self._database_connection)
        return db
