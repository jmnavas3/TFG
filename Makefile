
# variables de entorno obtenidas del .env

ifeq ("$(wildcard $(Docker/.env))","")
    -include Docker/.env
    export $(shell sed 's/=.*//' Docker/.env)
endif

# variables de .env por defecto
PROJECT_NAME=tfg
DATABASE=postgres
PYTHON_VERSION=3.10-rc-buster
NODE_VERSION=20-alpine
NPM_VERSION=10.8.2
NODE_ENVIRONMENT=development
WORKDIR= /app

# variables de docker
BUILDPROD	= -d --remove-orphans --build
RUNPROD 	= -f production.yml
RUNUP 	= --force-recreate --remove-orphans
RUNUPD 	= --force-recreate -d --remove-orphans
CDDK 	= cd Docker

# variables IDS
INTER			?= $(shell ip route | grep default | awk '{print $5}')
IDS_IMG_NAME	= "jasonish/suricata"
IDS_IMG_ID		=$(shell docker ps | grep "jasonish" | grep -Eo "^[[:alnum:]]{12}")
IDS_IMG_VER		= 7.0.6
SCRIPTS			= ./app/backend/scripts



all: help


help:						## Muestra la ayuda
	@awk 'BEGIN {FS = ":.*##"; printf "\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "	\033[36m%-26s\033[0m => %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

#---------- SERVIDOR (python y postgres) ----------
install:					## Instala en entorno .env de Docker
	export PROJECT_NAME=${PROJECT_NAME} && \
	export DATABASE=${DATABASE} && \
 	export PYTHON_VERSION=${PYTHON_VERSION} && \
    export NODE_VERSION=${NODE_VERSION} && \
    export NPM_VERSION=${NPM_VERSION} && \
    export NODE_ENVIRONMENT=${NODE_ENVIRONMENT} && \
 	export WORKDIR=${WORKDIR} && \
 	sh install.sh

build: install				## Construye los contenedores locales
	$(CDDK) && docker compose build

rebuild:					## Construye los contenedores locales
	$(CDDK) && docker compose build --no-cache

up:							## Levanta los contenedores locales y mantiene el stdout por pantalla
	$(CDDK) && docker compose up $(RUNUP)

up-d:						## Levanta los contenedores locales y deja libre la terminal
	$(CDDK) && docker compose up $(RUNUPD)

deploy: cronjob				## Levanta el IDS, los contenedores e inicia el servidor
	$(CDDK) && docker compose up $(RUNUPD)
	docker exec tfg_server sh deploy.sh

proxy:						## Crea la red del proxy-inverso para acceder por una regla de Traefik
	@docker network ls | grep -q proxy || docker network create proxy

run:
	$(CDDK) && docker compose $(RUNPROD) up $(BUILDPROD)

backend:
	$(CDDK) && docker compose $(RUNPROD) up reverse-proxy backend $(BUILDPROD)

end:
	$(CDDK) && docker compose $(RUNPROD) stop

exec:						## Ingresa por ssh al contenedor principal
	$(CDDK) && docker exec -ti $(PYTHONCONTAINER) /bin/bash

stop:						## Para los contenedores locales
	$(CDDK) && docker compose stop

down:						## Destruye los contenedores locales
	$(CDDK) && docker compose down -v --remove-orphans


#---------- IDS (suricata) ----------
info-ids:					## Ejemplo para ejecutar suricata en una interfaz de red
	@echo "Ejemplo con intefaz: make up-d INTER=<interfaz>"

install-ids:				## Instala la imagen de suricata
	docker pull $(IDS_IMG_NAME)

up-ids:						## Levanta la imagen de suricata, obtiene la configuración y mantiene el stdout por pantalla
	docker run --rm -itd --net=host --cap-add=net_admin --name=suricata --cap-add=net_raw --cap-add=sys_nice -v ./app/suricata/log/:/var/log/suricata $(IDS_IMG_NAME):$(IDS_IMG_VER) -i $(INTER)

up-rules:
	docker run -itd --rm --net=host --cap-add=net_admin --name=suricata --cap-add=net_raw --cap-add=sys_nice -v ./app/suricata/rules:/var/lib/suricata $(IDS_IMG_NAME):$(IDS_IMG_VER) -i $(INTER)
	docker cp $(SCRIPTS)/my_script.sh suricata:/
	docker cp $(SCRIPTS)/my_cron suricata:/etc/cron.d/
	docker exec suricata crontab /etc/cron.d/my_cron
	docker exec suricata crond -p

up-ids-d:					## Levanta la imagen de suricata y deja libre la terminal
	docker run -itd --rm --net=host --cap-add=net_admin --name=suricata --cap-add=net_raw --cap-add=sys_nice -v ./app/suricata/log:/var/log/suricata $(IDS_IMG_NAME):$(IDS_IMG_VER) -i $(INTER)

cronjob: run-multiple-vols
	docker cp $(SCRIPTS)/my_script.sh suricata:/
	docker cp $(SCRIPTS)/my_cron suricata:/etc/cron.d/
	docker exec suricata crontab /etc/cron.d/my_cron
	docker exec suricata crond -p

run-multiple-vols:			## Ejecuta la imagen de suricata en la interfaz de red indicada y guardando los logs y las rules
	docker run --rm -itd --name=suricata --net=host --cap-add=net_admin --cap-add=net_raw --cap-add=sys_nice \
	-v ./app/suricata/rules/:/var/lib/suricata/rules/copy \
	-v ./app/suricata/log:/var/log/suricata \
	$(IDS_IMG_NAME):latest -i $(INTER)

exec-ids:					## Ingresamos a la imagen de suricata
	docker exec -ti suricata /bin/bash

stop-ids:					## Paramos la imagen de suricata
	docker stop $(IDS_IMG_ID)
