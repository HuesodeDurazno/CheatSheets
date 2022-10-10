### syntax
0. type file (- regular file , d directory)
1. User permissions
2. Group permissions
3. Other permissions (en general)

### permissions sintaxis
1. r read
2. w write
3. x execute
4. "-" no otorgado
5. setuid (se ejecuta como si el propietario del archivo fuera el usuario creador en lugar de usted)

### cambiar permisos
    g by global , o by others
    chmod g+r file
    chmod o+r file

    chmod go+r file
    chmod go-r file

