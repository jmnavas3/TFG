ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION
RUN mkdir /config
COPY config/requirements.txt /
COPY config/config.yml /config/

RUN pip install --upgrade pip && pip install -r requirements.txt && pip install pytest pytest-cov

COPY app /app
WORKDIR /app

EXPOSE 5000