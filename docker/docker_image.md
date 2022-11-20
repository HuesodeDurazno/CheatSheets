# Dentro de dockerfile

## Ejecutar un commando en la creacion de la imagen
    RUN 

## Ejecutar un comando una vez terminada la creacion de la imagen
    CMD 

## Indicar la imagen base
    FROM

## Indicar directorio donde se ejecutaran comandos dentro del contenedor
    WORKDIR

## Copiar archivos del exteriro
    COPY [Path ext] [path Int]

## Indicar cuales puertos se tienen que compartir (solo es informativo)
    EXPOSE

## Agregar un volumen anonimo, solo para mantener informacion
    VOLUME ["PATH INT"]

## Crear variable de entorno
    ENV [name] [value]

## Uso de variables
    ej: EXPOSE $[name]

## uso de variables en docker
    ARG [name] [value]
    $name
 

### Nota: Al crear un docker es solo lecura, si se requiere hacer un cambio se tiene que volver a builder una imagen , Cada que agregamos un comando o caracteristica al contenedor , este se vuelve un layer , si se hace un cambio en algun layer , se rebuildean solo los layers posterior al que sufrio un cambio

## Nota los argumentos para build ARG  solo son aplicables en dockerfile
