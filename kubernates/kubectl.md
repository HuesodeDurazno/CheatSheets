## Obtener ayuda
    kubectl help

## crear un deployment object
    kubectl create deployment [name] --image=[ruta_dockerhub]

## Ver lista de objetos
    kubectl get 
                deployments
                pods
                services

## Eliminar objeto de cluster
    kubectl delete deployment [name]
                    service [name]

## Exponer un deployment como servicio
    kubectl expose deployment [name] --type=[ClusterIP,NodePort,LoadBalancer] --port=[port]

## Obtener external IP
    kubectl [name] 

## Escalar aplicaiones
    kubectl scale deployment/[name] --replicas=[number]

## Actualizar deployments
    kubectl set image deployment/[name] [current_container]=[new_image_path]

## realizar seguimiento a actualizacion
    kubectl rollout status deployment/[name] 

## DEshacer el ultimo deployment
    kubectl roullout undo deployment/[name]

## Ver deployments historicos
    kubectl rollout history deployment/[name]

## Ver detalles de un deploy
    kubectl rollout history deployment/[name] --revision=[number]

## Regresar a un deploy historico
    kubectl roullout undo deployment/[name] --to-revision=[number]

