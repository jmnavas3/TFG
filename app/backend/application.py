import logging
import sys
import threading
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from app.backend.intrusion_prevention_system import run_intrusion_prevention_system
from app.backend.flask_app import create_app

from app.backend.database.database import Database
from app.backend.configuration.configuration import Config

logger = logging.getLogger(__name__)


def run_flask_app():
    application = create_app()
    application.run(host="0.0.0.0", debug=True, use_reloader=False)


if __name__ == '__main__':
    config = Config.create("/config/config.yml").__dict__
    db = Database(config['SQLALCHEMY_DATABASE_URI'])

    flask_thread = threading.Thread(target=run_flask_app)
    watchdog_thread = threading.Thread(target=run_intrusion_prevention_system)

    flask_thread.start()
    watchdog_thread.start()

    flask_thread.join()
    watchdog_thread.join()
