import pytest
import os

from app.backend.application import create_app
from app.backend.configuration.configuration import Config
from app.backend.database.database import Database
from app.backend.src.base.infrastructure.middleware.mikrotik_middleware import MikrotikConnector
from app.backend.src.rules.infrastructure.repository.rules_repository import RulesRepository


@pytest.fixture()
def create_app_context():
    app = create_app()
    os.environ['FLASK_DEBUG'] = 'True'
    app.config['ENVIRONMENT'] = 'TESTING'
    app.app_context()
    yield app


@pytest.fixture()
def test_config():
    os.environ.setdefault("FLASK_ENV", "testing")
    config = Config.create('/config/config.yml')
    return config


@pytest.fixture()
def generate_database(create_app_context, test_config):
    with create_app_context.app_context():
        db = Database(db_url=test_config['SQLALCHEMY_DATABASE_URI'])
        db.get_db().init_app(create_app_context)
        database_item = {'session': db.session_factory(db=db), 'db': db}
        yield database_item


@pytest.fixture()
def router_connection():
    router_config = Config.create('/config/config.yml')["ROUTEROS"]
    connector = MikrotikConnector(router_ip=router_config["HOST"],
                                  username=router_config["USER"],
                                  password=router_config["PASSWORD"])
    yield connector


@pytest.fixture()
def repository(generate_database):
    return RulesRepository(session_factory=generate_database['session'])


@pytest.fixture()
def pagination():
    return {"page": 0, "per_page": 5}
