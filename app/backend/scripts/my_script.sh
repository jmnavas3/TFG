# script que se ejecutará en un cronjob cada minuto

LOG_FILE=/var/log/suricata/fast.log
CSV_FILE=/var/log/suricata/fast.csv

# curl para generar alerta de prueba en fast.log
curl http://testmynids.org/uid/index.html


# -------------------------------------------------------------------------
# SCRIPT PARA PASAR fast.log A fast.csv
if [ ! -f $LOG_FILE ]; then
    echo " no se encuentra el fast.log"
    return
fi

echo "fecha, identificador, prioridad, protocolo, ip_origen, puerto_origen, ip_destino, puerto_destino, alerta, clasificacion" > $CSV_FILE


# awk: lenguaje de regex para pasar fast.log a fast.csv
# sed: regex que convierte la fecha y la hora al formato yyyy-MM-dd HH:mm:ss para el tipo de dato datetime de python
awk '
{
    match($0, /([0-9]{2}\/[0-9]{2}\/[0-9]{4}-[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6})/, datetime);
    match($0, /\[\*\*\] \[([0-9]+:[0-9]+:[0-9]+)\]/, rule_id);
    match($0, /\]([-_[:alnum:][:space:]]*) \[\*/, alert_message);
    match($0, /\[Classification: ([[:alnum:][:space:]]+?)/, classification);
    match($0, /\[Priority: ([0-9]+)\]/, priority);
    match($0, /\{(\w+)\}/, protocol);
    match($0, /([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)/, source_ip);
    match($0, /([0-9]+) ->/, source_port);
    match($0, /-> ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+):([0-9]+)/, dest_ip_port);

    print datetime[1]", "rule_id[1]", "priority[1]", "protocol[1]", "source_ip[1]", "source_port[1]", "dest_ip_port[1]", "dest_ip_port[2]", "alert_message[1]", "classification[1];
}' $LOG_FILE | sed -E 's/([0-9]{2})\/([0-9]{2})\/([0-9]{4})-([0-9]{2}):([0-9]{2}):([0-9]{2})\.[0-9]{6}/\3-\2-\1 \4:\5:\6/' >> $CSV_FILE



# -------------------------------------------------------------------------
