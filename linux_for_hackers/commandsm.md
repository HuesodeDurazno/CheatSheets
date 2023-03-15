# Basic Commands in linux

Comandos basicos en linux

## Saber en que lugar te encuentras
    pwd

## Saber que usuario esta logeado
    whoami

## Navegacion en directorios
    cd
        moverte un nivel ..
        moverte n niveles ../..
                            ../../..
        moverte a raiz /

## Listar contenidos 
    ls
        listar un directorio en especifico ls etc/...\
        obtener detalles -l
        mostrar archivos ocultos -la , -l -a

## Obtener ayuda 
    [comand] -h,--help,-?

## Obtener manual pages
    man [command]

        Controls:
            Enter para hacer scroll
            arrow keys para moverse
            PG,DN Y PG,UP
            q para salir

# Busqueda
## Buscar en todo el filesystem
Se actualiza el lugar de busqueda diario

    locate [word]

##  Encontrar binarios con whereis
regresa origen y man page si esta disponible

    whereis [word]

## Encontrar binarios en la variablke Path

solo regresa ubicacion

    which [word]

## Busquedas mas poderosas con find

Basic sintax

    find [directory] [options] [expression]

Ejemplo

    find / -type f -name apache2

        buscar en la raiz , un archivo ordinario con el nombre apache2

        permite el uso de wildcards * . , ? []

## wildcards
    ? un solo caracter
    [x,y] remplaza por x o y
    * cualquier digito

## Filtrar con grep

se usa junto a una pipe para filtrar el resultado , por ejemplo ps nos muestra los procesos del sistema 

    ps aux

aux para especificar que process information mostrar, para filtrar por una palabra la salida de este comando se ocupa grep

    ps aux | grep apache2

# Modificar archivos y directiorios

## crear um archivo con cat 
se usa un redireccionamiento , se abre el modo interactivo para agregar contenido al archivo

    cat > [filename]
## mostrar contenido con cat

    cat [file]

## agregar contenido al archivo con cat

    cat >> [file]

## remplazar archivo con cat
solo se ocupa otra vez el comando cat con un redirect

    cat > [file]

## crar un arhivo con touch

    touch [filename]

## crear un directorio

    mkdir [name]

## copiar un archivo

    cp [ruta actual] [ruta deposito]

## renombrar o mover archivo o directorio

    mv [ruta actual] [ruta deposito]


## quitar un archivo

    rm [file]

## remover un directorio
El directorio tiene que estar vacio

    rm [directory]

## remover directorio y archivos
    rm -r [directorio]
