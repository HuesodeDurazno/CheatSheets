## Primeros pasos
```yaml
apiVersion: app/v1 #api version
kind: Deployment #Tipo de objeto a crear Service,Job,etc.
metadata:
    name: name # nombre del deployment
spec: # Especificaciones del deployment
    replicas: 1 #numero de replicas
    selector: 
        matchlabels: # key /value pods labels que queremos matchear
            app: app-second
        #matchExpressions:
    template: # nuevo objeto que indica algunas caracteristicas de los pods que seran creados
        metadata:
            labels:
                app: app-second
        spec: # Espicificaciones del pod
            containers:
                - name: container-1 #nombre del contenedor
                  image: ruta/container #Ruta de la imagen
                
```

## Aplicar primer deployment
    kubectl apply -f=[file.yaml]
