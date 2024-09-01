# desc: script para comentar o descomentar una línea de un archivo .rules
# author: jmnavas
# use: ./enable_disable_rule.sh <enable|disable> <rule_sid>

# ESTE SCRIPT ES EJECUTADO POR PYTHON


FILE=$3

test ! -z "$FILE" || FILE='/app/suricata/rules/suricata.rules'

# si no encuentra el SID en el directorio, termina el programa
grep -q "$2" "$FILE" || exit

if [ $1 = "enable" ]; then
	sed -i '/sid:'$2'/s/^# //' $FILE
	echo -n "enabled"
fi

if [ $1 = "disable" ]; then
  HABILITADA=$(grep "$2" "$FILE" | grep "#")
  test -z "$HABILITADA" || exit
	sed -i '/sid:'$2'/s/^/# /' $FILE
	echo -n "disabled"
fi
