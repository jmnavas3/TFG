#!/bin/bash

LOG_FILE=temp.log

# fecha
FECHA='^.{10}'

# solo sirve si se ejecuta después de FECHA_HORA
# ejemplo: grep -Eo "^.{26}" temp.log | grep -Eo "[[:digit:]:.]{15}"
FECHA_HORA='^.{26}'
HORA='[[:digit:]:.]{15}'

# obtiene el string: [1:2260005:1], procesar luego en python cada parte
# [ generador : id regla : revision de la regla ]
IDENTIFICACION='[[[:digit:]:]{2,}]'

# obtiene todo lo que hay entre los delimitadores [**] [**] y luego lo procesa
MENSAJE_1='\[\*\*\].*\[\*\*\]'
MENSAJE_2='[[:alpha:][:space:]]{2,}'

# obtiene la parte de SURICATA, ET INFO, etc. Hay que mejorarlo ya que en algunos casos coge de más 
MAYUS='[[:upper:][:space:]?_]{4,}'

# classification
# devuelve el mensaje con Classification incluido
CLASS_1='Classification: [[:alnum:][:space:]]*'

# prioridad (puede no existir en todos los casos, por eso se asigna un valor por defecto)
# PRIOR_DEF=4
PRIOR_1='Priority: [1234]?'
PRIOR_2='[[:digit:]]'

# protocolo
PROTOCOL_1='\{.+}'
PROTOCOL_2='[[:upper:]]+'

IP_PORT="[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}:[[:digit:]]+"


# borramos el archivo fast.csv si ya existe
if [ -f "fast.csv" ]; then
    rm "fast.csv"
fi

if [ -n "$1" ] && [ -f "$1" ]; then
    LOG_FILE=$1
fi

while read line; do
    # fecha-hora
    DATE=$(echo $line | grep -Eo "$FECHA")
    HOUR=$(echo $line | grep -Eo "$FECHA_HORA" | grep -Eo $HORA)
    # mensaje
    # echo $line | grep -Eo "$MENSAJE_1" | grep -Eo "$MENSAJE_2"
    # identificacion
    IDEN=$(echo $line | grep -Eo "$IDENTIFICACION")
    # prioridad
    PRIOR=$(echo $line | grep -Eo "$PRIOR_1" | grep -o "$PRIOR_2")
    # protocolo
    PROT=$(echo $line | grep -Eo "$PROTOCOL_1" | grep -Eo "$PROTOCOL_2")
    # ip y puerto origen
    ORIGEN=$(echo $line | grep -Eo "$IP_PORT" | head -1)
    # ip y puerto destino
    DESTINO=$(echo $line | grep -Eo "$IP_PORT" | tail -1)
    
    echo "$DATE, $HOUR, $IDEN, $PRIOR, $PROT, $ORIGEN, $DESTINO" >> fast.csv
done < $LOG_FILE
# echo $ORIGEN
# echo $DESTINO

# Línea de fast.log separada por datos
#
# fecha: 07/04/2024-18:13:56.905626
# delimitador: [**]
# identificación alerta: [1:2260005:1]
# mensaje de alerta: SURICATA Applayer Unexpected protocol
# delimitador 2: [**]
# clasificación: [Classification: Generic Protocol Command Decode]
# prioridad (1-4, siendo 1 más alta): [Priority: 3]
# protocolo de transporte: {TCP}
# direccion IP y puerto origen: 192.168.65.1:39339
# sentido: ->
# dirección IP y puerto destino: 192.168.65.7:2375

# formato de CSV (opciones):

# opcion 1
# fecha, identificacion, mensaje, clasificacion, prioridad, protocolo, ip_origen, puerto_origen, ip_destino, puerto_destino
# ejemplo
# 07/04/2024-18:13:56.905626, 1:2260005:1, SURICATA Applayer Unexpected protocol, Generic Protocol Command Decode, 3, TCP, 192.168.65.1, 39339, 192.168.65.7, 2375

# opcion 2
# fecha, hora, identificacion, mensaje, clasificacion, prioridad, protocolo, ip_origen, puerto_origen, ip_destino, puerto_destino
# ejemplo
# 07/04/2024, 18:13:56.905626, 1:2260005:1, SURICATA Applayer Unexpected protocol, Generic Protocol Command Decode, 3, TCP, 192.168.65.1, 39339, 192.168.65.7, 2375