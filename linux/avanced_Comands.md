# Comandos Avanzados

### Cambiar password
    passwd

### Variables de shell y de entorno
    Variables
    $ STUFF=[value]


    Variables de de entorno
    $ STUFF=blah
    $ export STUFF

### The command path
Esta variable contiene rutas donde se encuentran los comandos

    echo $PATH
    /usr/local/bin:/usr/bin:/bin

para sobre escribir esta variable , puedes
    
    $ PATH=dir:$PATH
    $ PATH=$PATH:dir

### Edicion en linea de comandos
|commands | descriptions |
|---------|--------------|
|CTRL-B | Move the cursor left |
|CTRL-F | Move the cursor right |
|CTRL-P | View the previous command (or move the cursor up) |
|CTRL-N | View the next command (or move the cursor down) |
|CTRL-A | Move the cursor to the beginning of the line |
|CTRL-E | Move the cursor to the end of the line |
|CTRL-W | Erase the preceding word |
|CTRL-U | Erase from cursor to beginning of line |
|CTRL-K | Erase from cursor to end of line |
|CTRL-Y | Paste erased text (for example, from CTRL-U) |

### Obtener documentacion
    man [command]
    
    buscar por palabra cable

    man -k keyword

    tambien: 

    [command] -h 
    [command] --help

    info [command]

### Shell input and output
    to a file
    command > file

    append insted override 
    command >> file

    connect process
    [command] | [command]

### Modificar output de shell
modifica el estandar por e , 2 es el stream id 

Stream ID
1 is standard output (the default), and 2 is standard err
or.
You can also send the standard error to the same place as stdout with
the >& notation. For example, to send both standard output 
and standard

error to the file named f, try this command:
    
    ls /fffffffff > f 2> e

    ls /fffffffff > f 2>&1

### canalizar a un archivo a la program's standart imput
    head < /proc/cpuinfo


