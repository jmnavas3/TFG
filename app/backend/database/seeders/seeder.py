import os

from ..database import Database, Base
from ...configuration.configuration import Config


class SeederDB:
    entity = None

    def __init__(self, db=None, environment: str = 'testing'):
        os.environ['FLASK_ENV'] = environment.upper()
        self._db = Database(db_url=Config.create('/config/config.yml')["SQLALCHEMY_DATABASE_URI"])
        if db is not None:
            self._db = db
        self._db.create_database()

    def get_db(self) -> Database:
        return self._db

    def drop_all(self) -> None:
        Base.metadata.drop_all(bind=self._db.get_engine())

    def drop_entities(self):
        with self._db.session_factory(db=self._db)() as session:
            try:
                session.query(self.entity).delete()
            except Exception as info:
                raise Exception(str(info))
            session.commit()
        self.create_database()

    def create_database(self) -> None:
        self.get_db().create_database()
