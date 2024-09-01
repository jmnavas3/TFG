# desc: script para añadir un nuevo archivo .rules al IDS
# author: jmnavas
# use: ./add_rule_file.sh <new_rules_file> <rules_file>

# ESTE SCRIPT ES EJECUTADO POR PYTHON


NEW_RULES_FILE=$1
RULES_FILE=$2

# valor por defecto si no existe el archivo
test -f "$RULES_FILE" || RULES_FILE="/app/suricata/rules/suricata.rules"
test ! -z "$NEW_RULES_FILE" || exit

if [ -f "$NEW_RULES_FILE" ]; then
 echo >> "$RULES_FILE"
 cat "$NEW_RULES_FILE" >> "$RULES_FILE"
# rm "$NEW_RULES_FILE"
 echo -n "done"
fi