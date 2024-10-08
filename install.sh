#!/bin/bash

ENV_FILE=Docker/.env

# Si existe el archivo de environment lo borramos
if [ -e $ENV_FILE ]; then
  rm $ENV_FILE
fi


# Creamos el archivo .env
touch $ENV_FILE

# Exportamos las variables al archivo .env
echo "ROOT="$(pwd) | tee -a "$ENV_FILE"
echo "WORKDIR=${WORKDIR}" | tee -a "$ENV_FILE"

echo "COMPOSE_PROJECT_NAME=${PROJECT_NAME}" | tee -a "$ENV_FILE"
echo "PYTHONCONTAINER=${PROJECT_NAME}_server" | tee -a "$ENV_FILE"
echo "POSTGRESCONTAINER=${PROJECT_NAME}_db" | tee -a "$ENV_FILE"

echo "SERVERNAME=${PROJECT_NAME}" | tee -a "$ENV_FILE"
echo "DOMAIN=localhost" | tee -a "$ENV_FILE"
echo "PYTHON_VERSION='${PYTHON_VERSION}'" | tee -a "$ENV_FILE"

echo "POSTGRES_USER=postgres" | tee -a "$ENV_FILE"
echo "POSTGRES_PASSWORD=password" | tee -a "$ENV_FILE"
echo "POSTGRES_DB=${DATABASE}" | tee -a "$ENV_FILE"
echo "POSTGRES_SERVICE=${DATABASE}" | tee -a "$ENV_FILE"

echo "ROUTEROS_HOST=192.168.1.1" | tee -a "$ENV_FILE"
echo "ROUTEROS_USER=admin" | tee -a "$ENV_FILE"
echo "ROUTEROS_PASS=password" | tee -a "$ENV_FILE"