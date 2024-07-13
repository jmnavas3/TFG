from flask import Flask
from backend.configuration.configuration import Config
from backend.routes.api import api_route


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api_route, url_prefix="/api")
    app.config.from_object(Config.create('/config/config.yml'))
    return app

if __name__ == '__main__':
    application = create_app()
    application.run(host='0.0.0.0')
