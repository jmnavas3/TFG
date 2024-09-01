#export FLASK_APP=backend.application
#export FLASK_DEBUG=True
python backend/intrusion_prevention_system.py &
sh wsgi/gunicorn.sh
