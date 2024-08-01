cd backend/database
export FLASK_APP=db_migrate
export FLASK_DEBUG=True
flask db "$1"