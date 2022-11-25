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

## renombrar archivo 
    git mv [file] [new name]

## eliminar con git
    git rm [file]

## deshacer al ultimo commit x2
    git reset --hard

## crear una rama 
    git branch [name]

## cambiar de rama
    git checkout [name]

## hacer merge
    estar en la rama a la que queremos agregar cambios
    git merge [branch_name]

## eliminar rama 
    git branch -d [nombre de la rama]
                                -f eliminar de manera forzada

## crear y cambiar
    git chekout -b [branch name]

## crear tag
    git tag [name]

## crear tag con version semantica
    git tag -a v1.0.0 -m "[message]"
        1 cambios mayores
        0 agregando funcionalidad
        0 bug fix

## tagear commits anteriores
    git tag -a [version] [hash commit] -m "[message]"

## ver tags
    git tag

## ver detalle de tag
    git show [version]

## crear stash
ultimos cambios antes del ultimo commit

    git stash

## ver referencias al stash
    git stash list

## recuperar los cambios del ultimo stash
    git stash pop

## conflicto en el stash
    resolver conflicto y commit

## aplicar un stash en especifico
    git stash apply [stash]

## borrar stash
    git stash drop [stash]
                    sin parametros es el ultimo

## ver stash pero no aplicar 
    git stash show [stash]

## guardar stash con nombre
    git stash save "[name]"

## ver mas detalle de los stash
    git stash list --stat

## borrar stashes
    git stash clear

## rebase
    en la rama donde queremos hacer el rebase

    git rebase master

    pasa la rama al ultimo commit de master 

## juntar commits
    git rebase -i HEAD~4 o hash
        abrirar un menu interactivo para hacer varias acciones 


## retornar solo un archivo a el ultimo commit
    git checkout -- [path]

# pushear tags
    git push --tags

# obtener datos desde github
    git pull 

# ver en que ruta remota esta su repositorio
    git remote -v

# ver repositorios remotos
    git remote 

# actualizar las referencias locales
    git fetch