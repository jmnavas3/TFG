ARG PYTHON_VERSION=3.10-rc-buster
FROM python:$PYTHON_VERSION
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /app /var/log/supervisor

RUN mkdir /config
COPY config/config.yml /config/

COPY app /app
#WORKDIR /app

COPY app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY config/requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

#CMD ["sh", "wsgi/gunicorn.sh"]
CMD ["/usr/bin/supervisord"]