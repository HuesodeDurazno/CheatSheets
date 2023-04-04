## Obtener el head del archivo
    head {path}

        Solo muestra las primeras 10 lineas
    
        -[number] ver las n lineas
## Obtener las ultimas lineas del arhcivo
    tail [path]
        -[number] ver las n ultimas linenas, si no se agrega muestra los ultimos dies

## Mostrar archivo con numero de linea 
    nl [path]

## buscar y remplazar palabras
    sed s/[palabra a remplazar]/[palabra nueva]/g 
                    /g -> se aplican los cambios globalmente
                    / -> solo se aplicara a la primera incidencia
                    /[number] -> se aplica a la n concidencia

    para guardar en un nuevo archivo escribir > 

## mostrar un display a las vez, tambien indica el porcentaje del archivo
    more [path]

##  mostrar display y filtrar
    less [path]
        presiona / para buscar
            /[word]
        
        n -> siguiente incidencia
        