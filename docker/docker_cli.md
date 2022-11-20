# Docker 

## Mostrar los contonedores corriendo
    docker ps
        -a ver tambien los detenidos

## Detener contenedor
    docker stop [name/hash]

## Iniciar un contenedor
crea un layer en la imagen y empieza el contenedor
    
    docker run [image]
        -p [port]:[port] Comparte puertos con la imagen original

        -d detacher mode , en el background

        -it sesion interactiva

        -rm eliminar contenedor al detenerse

        --name [name] agregar nombre al contenedor

        -v 
            [path ext/name]:[path int] agregar un bind mount 
            
            [path] volumen anonimo
            
            [path ext/name]:[path int]:ro volumen de lectura solamente
        
        --e o -e [Name] = [value]
            agregar variable de entorno
        
        --env-file [path]
            archivo con variables de entorno
        
        --build-arg [var name] = [value]

        --network [name]

## buildear una imagen desde dockerfile
    docker build [path]
        -t [name]:[tag] [path]
            agregamos tag a una imagen

## Ver ayuda
    docker [command] --help

## reinicia un docker que se detuvo en el pasado
    docker start
        -a attached mode
        -i sesion interactiva
    

## ejecutar en attached mode 
    docker attach [id / name]

## ver los logs de una imagen
    docker logs
        -f seguir los logs

## Eliminar contenedores
    docker rm [id/name]

## ver imagenes
    docker images

## Eliminar imagenes
    docker rmi [id/name]

## Eliminar imagenes no utilizadas
    docker image prune
        -a borra imagenes sin un contenedor

## Ver informacion detallada de una o varias imagenes
    docker image inspect [id/name]

## Copiar informacion de docker a local
    docker cp [path] [id/name]:[path]
        de local a contenedor
    docker cp [id/name]:[path] [path]
        de contenedor a local

## subimos docker a docker hub
    docker push [path]

## renombrar un docker con tag, se quedan las dos imagenes
    docker tag [id/name]:[tag] [new name]

## Iniciar sesion en docker hub
    docker login

## traer una imagen de docker hub
    docker pull [path]

## borrar un volumen 
    docker volume rm [vol name]

## eliminar todos los volumenes no usados
    docker volume prune

## listar todas las imagenes
    docker image ls

## crear volumen
    docker volume create 

## detalles de un volumen
    docker volume inspect [name/id]

## crear una network
    docker network [name] 
                    ls lista las redes

