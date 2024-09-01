<<<<<<< HEAD
=======
import logging
from pathlib import Path
import threading
import time
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from app.backend.src.alerts.infrastructure.services.import_csv_service import AlertRepository, \
    CambioArchivoHandler
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324
from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

<<<<<<< HEAD
from backend.database.database import Database
from backend.containers import Container
from backend.configuration.configuration import Config
from backend.routes.api import api_route, readiness_route
=======
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from app.backend.database.database import Database
from app.backend.containers import Container
from app.backend.configuration.configuration import Config
from app.backend.routes.api import api_route, readiness_route


logger = logging.getLogger(__name__)
ALLOWED_EXTENSIONS = {'txt', 'csv'}


# obtenemos ruta al directorio app
try:    
    path_root = str(Path(__file__).parents[1])
    # print(path_root)
    csv_path = f'{path_root}/suricata/log/fast.csv'
    file_path = f'{path_root}/suricata/log/fast.csv'
except Exception as e:
    print(e)
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324


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

<<<<<<< HEAD
if __name__ == '__main__':
    application = create_app()
    application.run(host='0.0.0.0')
=======

def run_watchdog():
    repo = AlertRepository(Database.session_factory(db=db))
    event_handler = CambioArchivoHandler(repo, csv_path, file_path)
    observer = Observer()
    observer.schedule(event_handler, file_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def run_flask_app():
    application = create_app()
    application.run(host="0.0.0.0", debug=True, use_reloader=False)


if __name__ == '__main__':

    config = Config.create("/config/config.yml").__dict__
    db = Database(config['SQLALCHEMY_DATABASE_URI'])

    flask_thread = threading.Thread(target=run_flask_app)
    watchdog_thread = threading.Thread(target=run_watchdog)

    flask_thread.start()
    watchdog_thread.start()

    flask_thread.join()
    watchdog_thread.join()

    # application = create_app()
    # application.run(host='0.0.0.0')
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324
