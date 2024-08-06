import logging
from pathlib import Path
import threading
import time

from backend.src.alerts.infrastructure.services.import_csv_service import CambioArchivoLine
from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from backend.database.database import Database
from backend.containers import Container
from backend.configuration.configuration import Config
from backend.routes.api import api_route, readiness_route

logger = logging.getLogger(__name__)

# obtenemos ruta al directorio app
try:    
    path_root = str(Path(__file__).parents[1])
    print(path_root)
    csv_path = f'{path_root}/suricata/log/fast.csv'
    file_path = f'{path_root}/suricata/log/fast.log'
    handler = CambioArchivoLine(file_path, csv_path)
    handler.start()
except Exception as e:
    print(e)


def worker():
    observer_out = Observer()
    observer_out.schedule(handler, path=file_path, recursive=False)
    observer_out.start()
    
    try:
        while True:
            print("hola mundo!")
            time.sleep(1)
    except Exception as e:
        print(str(e))
        observer_out.stop()
    observer_out.join()


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
    # Create and start a new thread
    # thread = threading.Thread(target=worker)
    # thread.start()
    
    observer_out = Observer()
    observer_out.schedule(handler, path=file_path, recursive=False)
    observer_out.start()
    
    try:
        while True:
            print("hola mundo!")
            time.sleep(1)
    except Exception as e:
        print(str(e))
        observer_out.stop()
    observer_out.join()

    application = create_app()
    application.run(host='0.0.0.0')
    # thread.join()
