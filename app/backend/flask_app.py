import sys
from pathlib import Path

from app.backend.src.firewall.infrastructure.container.firewall_container import FirewallContainer

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from injector import Injector

from app.backend.database.database import Database
from app.backend.configuration.configuration import Config
from app.backend.src.alerts.infrastructure.container.alerts_container import AlertsContainer
from app.backend.src.rules.infrastructure.container.rules_container import RulesContainer
from app.backend.routes.api import api_route
from app.backend.routes.readiness import readiness_route


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(api_route, url_prefix="/api")
    app.register_blueprint(readiness_route, url_prefix="/readiness")
    app.config.from_object(Config.create('/config/config.yml'))

    db = Database(app.config['SQLALCHEMY_DATABASE_URI'])
    injector = Injector([
        AlertsContainer(app.config["SQLALCHEMY_DATABASE_URI"]),
        RulesContainer(app.config["SQLALCHEMY_DATABASE_URI"], app.config["NEW_RULES"]),
        FirewallContainer(app.config["ROUTEROS"]),
    ])

    FlaskInjector(app=app, injector=injector)

    @app.teardown_appcontext
    def shutdown_session(exception):
        db.get_session().remove()

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(host="0.0.0.0", debug=True, use_reloader=False)
