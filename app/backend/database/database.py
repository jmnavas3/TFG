from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging

from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import Session, sessionmaker, scoped_session, declarative_base
from flask_sqlalchemy import SQLAlchemy


logger = logging.getLogger(__name__)
Base = declarative_base()
db = SQLAlchemy()

class Database:
    def __init__(self, db_url: str) -> None:
        self._db = SQLAlchemy()
        self._db_url = db_url
        self._engine = create_engine(url=self._db_url, echo=False, connect_args={"options": '-c timezone=utc'})
        self._session_factory = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    def get_db(self):
        return self._db

    def get_engine(self):
        return self._engine

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        self._engine = create_engine(url=self._db_url, echo=False, poolclass=NullPool, connect_args={"options": '-c timezone=utc'})
        session: Session = scoped_session(sessionmaker(autoflush=True, bind=self._engine))()

        try:
            session.connection()
            yield session
        except Exception as e:
            logger.exception(f"Session rollback because of exception: {e}")
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def session_factory(db):
        return db.session

    def get_session(self):
        return self._session_factory
