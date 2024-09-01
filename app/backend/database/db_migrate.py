<<<<<<< HEAD
from backend.application import create_app
=======
from app.backend.flask_app import create_app
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = create_app()
app.app_context()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
