# desc: script para comentar o descomentar una línea de un archivo .rules
# author: jmnavas
# use: ./enable_disable_rule.sh <enable|disable> <rule_sid>

# ESTE SCRIPT ES EJECUTADO POR PYTHON


FILE='/app/suricata/rules/suricata.rules'

# si no encuentra el SID en el directorio, termina el programa
grep "$2" "$FILE" || exit

if [ $1 = "enable" ]; then
	sed -i '/sid:'$2'/s/^# //' $FILE
fi

if [ $1 = "disable" ]; then
	sed -i '/sid:'$2'/s/^/# /' $FILE
fi
