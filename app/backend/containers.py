from injector import Module, Binder, singleton
from backend.database.database import Database


class Container(Module):
    def __init__(self, database_connection: str = ''):
        self._database_connection = database_connection

    def configure_db(self):
        db = Database(self._database_connection)
        return db

    def configure(self, binder: Binder) -> None:
        db = self.configure_db()
        binder.bind(Database, to=db, scope=singleton)
