#!/bin/bash

archivo_paginas="./paginas.txt"
if [ ! -f "$archivo_paginas" ]; then
    echo "No se encontro el archivo $archivo_paginas. Tenes que estar parado en el mismo directorio"
    exit 1
fi

while IFS= read -r url; do
    xdg-open "$url"
done < "$archivo_paginas"

