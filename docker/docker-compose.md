# agregar archivo de variables de entorno
    env_file:
        - [path]

# volumenes
    volumes:
        - [path ext]:[path int]

# imagen que ocupara
    image: '[name]'

# agregar varibles de entorno
    enviroment:
        [name variable]:[value]

# levantar docker
    docker-compose up 
        -d deteache mode
        --build obligas a que se buildeen las imagenes
# tirar docker
    focker-compose down
        -v elimina volumenes
# construir con docker file
    build: [path]
    build:
        context:[path]
        dockerfile:[path]
        args:
            [variable]:[value]
# puertos
    ports:
        - '[ext port]:[int port]'
# dependencia de un contenedor anterior
    depends_on:
        - [name]

# sesion interactiva
    stdin_open: true
    tty: true

# buildear imagenes sin correr
    docker-compose build
