# Comandos Basicos

## Version de git 
    git --version

## wiki
    git help

## agregar nombre de usuario y correo
    git config --global user.name "[nombre]"
    git config --global user.email "[email]"

## inicializar el repo
    git init 

## cambiar nombre rama principal 
    git config --global init.DefaultBranch [name]
    git branch -m [name last] [new name]

## informacion sobre git 
    git status

## agregar seguimiento
    git add [file]
        . agregar todo

## remover del stage
    git reset [file]

## hacer un commit 
    git commit -m "[message]"
                -am  agregar todo al stage y commit


## regresar al ultimo commit 
    git checkout -- .

## listar ramas
    git branch

## entrar a la config global 
    git config --global -e

## ver logs
    git logs

## mantener carpetas vacias
    .gitkeep