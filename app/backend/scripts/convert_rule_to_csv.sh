# desc: convierte un archivo .rules a .csv con las columnas rule, sid, rev y msg
# author: jmnavas
# use: sh convert_rule_to_csv.sh <rules_file> <csv_file>

# ESTE SCRIPT ES EJECUTADO POR PYTHON


RULES_FILE=$1
CSV_FILE=$2

# comprueba que existe el archivo de reglas
test -f "$RULES_FILE" || exit
# comprueba que la variable CSV_FILE no está vacía
test ! -z "$CSV_FILE" || CSV_FILE="prueba.csv"

awk '
BEGIN {
    FS="[();]"
    OFS=","
    print "rule,sid,rev,msg,active"
}

# Función para eliminar espacios en blanco al inicio y al final de la cadena
function trim(s) {
    gsub(/^[ \t\r\n]+|[ \t\r\n]+$/, "", s)
    return s
}

{
    # Ignorar líneas comentadas y líneas vacías
    if ($0 ~ /^[ \t]*#/ || $0 ~ /^[ \t]*$/) {
        next
    }

    rule = $1
    sid = ""
    rev = ""
    msg = ""

    for (i = 2; i <= NF; i++) {
        if ($i ~ /sid:/) {
            sub(/sid:/, "", $i)
            sid = trim($i)
        } else if ($i ~ /rev:/) {
            sub(/rev:/, "", $i)
            rev = trim($i)
        } else if ($i ~ /msg:/) {
            sub(/msg:"/, "", $i)
            sub(/"$/, "", $i)
            msg = trim($i)
            msg = "\"" msg "\""
        }
    }

    if (sid != "" && rev != "") {
        print trim(rule), sid, rev, msg, "True"
    }
}' "$RULES_FILE" > $CSV_FILE
