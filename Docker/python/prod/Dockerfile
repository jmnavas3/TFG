ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION
RUN mkdir /config
COPY config/requirements.txt /
COPY config/config.yml /config/

RUN pip install --upgrade pip && pip install -r requirements.txt && pip install pytest pytest-cov

COPY app /app
WORKDIR /app

<<<<<<< HEAD
EXPOSE 5000
=======
EXPOSE 5000

CMD ["sh", "wsgi/gunicorn.sh"]
>>>>>>> d21db116366befdb866ac9b45065c3c981d67324
