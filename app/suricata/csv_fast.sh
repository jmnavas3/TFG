#!/bin/bash
# almacena en un archivo csv la salida del archivo fast.log
# OBSOLETO
# SE HA MOVIDO A app.backend.scripts

LOG_FILE=./fast.log
CSV_FILE=./data.csv

if [ ! -f $LOG_FILE ]; then
    return
fi

echo "Fecha, Identificador, Prioridad, Protocolo, Origen, Destino, Alerta, Clasificacion" > $CSV_FILE

awk '
{
    match($0, /([0-9]{2}\/[0-9]{2}\/[0-9]{4}-[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6})/, datetime);
    match($0, /\[\*\*\] \[([0-9]+:[0-9]+:[0-9]+)\]/, rule_id);
    match($0, /\]([-_[:alpha:][:space:]]*) \[\*/, alert_message);
    match($0, /\[Classification: ([[:alnum:][:space:]]+?)/, classification);
    match($0, /\[Priority: ([0-9]+)\]/, priority);
    match($0, /\{(\w+)\}/, protocol);
    match($0, /([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)/, source_ip_port);
    match($0, /-> ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)/, dest_ip_port);

    print datetime[1]", "rule_id[1]", "priority[1]", "protocol[1]", "source_ip_port[1]", "dest_ip_port[1]","alert_message[1]", "classification[1];
}' $LOG_FILE >> $CSV_FILE
