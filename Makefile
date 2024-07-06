
RUNUP 	= --force-recreate --remove-orphans
RUNUPD 	= --force-recreate -d --remove-orphans
CDDK 	= cd Docker
CDIDS 	= cd suricata
TRAEFIK	= $(shell find ../Informatica/TFG/ -type d -name "traefik")
CDTK	= cd $(TRAEFIK)
INTER	?= eth0
IMAGE	= "jasonish/suricata"
IMAGEID	=$(shell docker ps | grep "jasonish" | grep -Eo "^[[:alnum:]]{12}")
IMG_VER	= 7.0.6


help:						## Muestra la ayuda
	@awk 'BEGIN {FS = ":.*##"; printf "\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "	\033[36m%-26s\033[0m => %s\n", $$1, $$2 }' $(MAKEFILE_LIST)


info:						## Ejemplo para ejecutar suricata en una interfaz de red
	@echo "Ejemplo con intefaz: make up-d INTER=<interfaz>"

install:					## Instala la imagen de suricata
	docker pull $(IMAGE)

up-tk:						## Levanta el contenedor del proxy inverso, traefik
	$(CDTK) && docker compose up -d

up:							## Levanta la imagen de suricata y mantiene el stdout por pantalla
	docker run --rm -it --net=host --cap-add=net_admin --name=suricata --cap-add=net_raw --cap-add=sys_nice $(IMAGE):$(IMG_VER) -i $(INTER)

up-d:						## Levanta la iamgen de suricata y deja libre la terminal
	docker run -d --rm -it --net=host --cap-add=net_admin --cap-add=net_raw --cap-add=sys_nice -v $(shell pwd)/suricata/log:/var/log/suricata $(IMAGE):$(IMG_VER) -i $(INTER)

exec:						## Ingresamos por ssh a la imagen de suricata
	docker exec -ti $(IMAGEID) /bin/bash

stop:						## Paramos la imagen de suricata
	docker stop $(IMAGEID)

stop-tk:					## Paramos el contenedor de traefik
	$(CDTK) && docker compose stop

