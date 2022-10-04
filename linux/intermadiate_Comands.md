## Comandos intermedios

### lineas que hacen match en un archivo
    grep [text] [path file]
        -i --> match insesntive
        -v --> invierte la busqueda ,aquellas que no tienen el match
        -E --> con expresiones regulares

### Ver el archivo en pantalla completa uno a la vez
    less [path file]
        [spacebar] --> avanzar
        b --> regresar
        q --> salir
    more 
        mismo comando pero en otras distros
    
    se puede conectar con una pipe

     grep ie /usr/share/dict/words | less

### ruta del directorio actual
si aplicas la bandera -P obtienes el full path real
    
    pwd 

### ver diferencias entre archivos
    dif [file1] [file2]
    -u  formato adecuado para enviar a otros procesos

### ver formato de un archivo
    file [file]

### Localizar un archivo
    find [dir] -name [fle] -print
    locate

### ver cabeza o cola deun archivo
    head [filepath]
    tail [filepath]
        -n --> lines to show
        +n --> empezar en la linea n

### ordenar las lineas de un archivo
    sort
        -n numeric sort
        -r reverse sort
