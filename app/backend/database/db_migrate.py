from app.backend.application import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = create_app()
app.app_context()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
