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

## agregar alias 
    git config --global alias.[alias] [command]

    alias recomendados:
        s "status --short"

        lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"

        s status -sb

## ver cambios que se hicieron desde el ultimo commit
    git diff --> cambios que no estan en el stage
            --staged --> cambios que estan en el stage

## cambiar nombre comit anterior 
    git commit --amend -m "[message]"

## deshacer commit no destructivo
    git reset --soft HEAD^
                        [hash de commit]
                        ^[numero] n commits atras

## deshacer un commit no detructivo
    git reset --mixed [lo mismo que soft]
    
    olvida los commits  y el trackeo pero no elimina archivos

## deshacer un commit , destructivo
    git reset --hard [lo mismo que anteriores]

## ver referencia de cambios futuros y pasados
    git reflog 
     
    despues volver a moverte a git futuro con git reset --hard
