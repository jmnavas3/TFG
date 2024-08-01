from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

from backend.database.database import Database
from backend.containers import Container
from backend.configuration.configuration import Config
from backend.routes.api import api_route, readiness_route


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api_route, url_prefix="/api")
    app.register_blueprint(readiness_route, url_prefix="/readiness")
    app.config.from_object(Config.create('/config/config.yml'))
    
    db = Database(app.config['SQLALCHEMY_DATABASE_URI'])
    injector = Injector([
        Container(app.config["SQLALCHEMY_DATABASE_URI"])
    ])

    FlaskInjector(app=app, injector=injector)

    @app.teardown_appcontext
    def shutdown_session(exception):
        db.get_session().remove()

    return app

if __name__ == '__main__':
    application = create_app()
    application.run(host='0.0.0.0')
