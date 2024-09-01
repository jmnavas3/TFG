#!/bin/sh
gunicorn --log-config /app/wsgi/gunicorn_logging.conf --chdir /app/backend backend:app -w 2 --threads 2 -b 0.0.0.0:5000
