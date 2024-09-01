from pathlib import Path
import sys

"""imports"""
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from app.backend.flask_app import create_app

app = create_app()
