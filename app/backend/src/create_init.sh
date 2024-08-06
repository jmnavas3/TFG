#!/bin/bash

# Función para crear el archivo __init__.py si no existe
create_init() {
    local dir=$1
    if [ ! -f "$dir/__init__.py" ]; then
        touch "$dir/__init__.py"
        echo "Creado: $dir/__init__.py"
    fi
}

# Exportar la función para que pueda ser usada por find
export -f create_init

# Usar find para buscar directorios y llamar a la función create_init
find . -type d -exec bash -c 'create_init "$0"' {} \;
