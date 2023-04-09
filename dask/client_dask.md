## El cliente de dask

El cliente de Dask se utiliza para enviar tareas y distribuir el trabajo a través de un clúster de nodos. El cliente actúa como intermediario entre el usuario y el clúster. Permite al usuario monitorear y controlar el progreso de las tareas, obtener resultados intermedios, diagnosticar problemas y más.

Para usar el cliente de Dask, primero se debe crear un objeto Client:

```python
    from dask.distributed import Client

    client = Client()
```

Este objeto Client conecta al usuario con un clúster de nodos, que se puede ejecutar localmente en una sola máquina o en un clúster distribuido en una red de múltiples máquinas.

Una vez que se crea el objeto Client, el usuario puede enviar tareas para procesar en el clúster. Las tareas se envían a través de las funciones proporcionadas por Dask, como dask.delayed o dask.bag, que dividen la tarea en partes más pequeñas y distribuyen el trabajo entre los nodos.

## interfaz grafica

El cliente de Dask también proporciona una interfaz de usuario web para monitorear y controlar el progreso de las tareas. Para acceder a esta interfaz, simplemente se debe ejecutar:


```python
    client
```

## Dask client en dask df y dask array

Al instanciar el cliente de dask , este cliente sera ocupado por los dask df y dask  array para enviar tareas al cluster local.

Es importante cerrar el cliente de Dask al finalizar el trabajo para liberar los recursos y evitar fugas de memoria.

```
    client.close()
```

## Clusters compatibles con el dask Client

El Dask Client es compatible con una amplia variedad de tipos de clústeres, que van desde un clúster local de un solo nodo hasta un clúster distribuido de múltiples nodos en una infraestructura de nube o en un centro de datos. A continuación se describen algunos de los tipos de clústeres que son compatibles con el Dask Client:

1. Clúster local: El Dask Client se puede ejecutar en un clúster local de un solo nodo. En este caso, el cliente distribuye el trabajo entre los núcleos disponibles en el nodo local utilizando la multiprocesamiento.

2. Clúster distribuido: El Dask Client se puede ejecutar en un clúster distribuido de múltiples nodos. En este caso, el cliente se conecta a un planificador centralizado y envía tareas a los trabajadores distribuidos en los nodos del clúster.

3. Clúster en la nube: El Dask Client se puede ejecutar en un clúster en la nube, como Amazon Web Services (AWS) o Google Cloud Platform (GCP). En este caso, el cliente se conecta a un clúster de nodos de cómputo en la nube y distribuye el trabajo entre ellos.

4. Clúster en un centro de datos: El Dask Client se puede ejecutar en un clúster de nodos en un centro de datos. En este caso, el cliente se conecta a un clúster centralizado y envía tareas a los nodos de cómputo.

En general, cualquier clúster que admita Python y que tenga acceso a la red y al almacenamiento compartido es compatible con el Dask Client. El tipo de clúster que se debe utilizar depende del tamaño de los datos y la complejidad del trabajo que se va a realizar. Para trabajos pequeños y medianos, un clúster local o distribuido puede ser suficiente, mientras que para trabajos grandes y complejos, es posible que se requiera un clúster en la nube o en un centro de datos.

## Clusters distribuidos recomendados

Algunos ejemplos de clústeres distribuidos populares que se pueden utilizar con el Dask Client son:

Kubernetes: Kubernetes es un sistema de orquestación de contenedores que se puede utilizar para crear y administrar clústeres distribuidos de Dask. Kubernetes permite escalar fácilmente el clúster de Dask, agregar o quitar nodos según sea necesario y administrar recursos.

Apache Mesos: Apache Mesos es un sistema de gestión de clústeres que se puede utilizar para crear y administrar clústeres distribuidos de Dask. Mesos es escalable y puede ejecutarse en una variedad de entornos, desde centros de datos hasta nubes públicas y privadas.

Hadoop: Hadoop es un marco de trabajo distribuido para el almacenamiento y procesamiento de grandes conjuntos de datos. Dask se puede ejecutar en un clúster distribuido de Hadoop utilizando la biblioteca Hadoop Distributed File System (HDFS) para el almacenamiento de datos.

AWS: Amazon Web Services (AWS) es un proveedor de servicios en la nube que ofrece varios servicios que se pueden utilizar para crear y administrar clústeres distribuidos de Dask. Por ejemplo, Amazon Elastic Kubernetes Service (EKS) se puede utilizar para ejecutar clústeres de Dask en Kubernetes, mientras que Amazon Elastic MapReduce (EMR) se puede utilizar para ejecutar clústeres de Dask en Hadoop.

En resumen, la elección del clúster distribuido más adecuado para el Dask Client depende de factores como la escala de los datos, la cantidad de recursos disponibles, la infraestructura de la empresa, la complejidad del trabajo, y la preferencia personal.

## Conectar el dask client a un EKS (Puede ser una opcion)

Para conectar el Dask Client a un clúster de Amazon Elastic Kubernetes Service (EKS), se pueden seguir los siguientes pasos:

1. Configurar el clúster EKS: Primero, se debe configurar un clúster de EKS y desplegar Dask en el clúster. Esto se puede hacer utilizando una plantilla de CloudFormation o una herramienta de gestión de infraestructura como Terraform.

2. Obtener las credenciales de acceso al clúster: Para conectarse al clúster de EKS desde el Dask Client, se necesitan las credenciales de acceso al clúster. Estas credenciales incluyen el nombre del clúster, la región de AWS y las credenciales de AWS IAM.

3. Instalar el paquete kubernetes: El paquete kubernetes de Python debe estar instalado para que el Dask Client se pueda conectar al clúster de EKS. Esto se puede hacer mediante la ejecución del siguiente comando en una terminal de Python:

```bash
    !pip install kubernetes
```

4. Crear una conexión de cliente: Se debe crear una conexión de cliente de Dask utilizando la clase Client de Dask. Para conectarse a un clúster de EKS, se debe especificar la dirección URL del clúster y las credenciales de acceso en el argumento address. Por ejemplo:

```python
    from dask.distributed import Client
    from dask_kubernetes import KubeCluster

    cluster = KubeCluster.from_yaml('cluster.yaml')
    client = Client(address=cluster.scheduler_address)
```

En este ejemplo, cluster.yaml es un archivo YAML que contiene la configuración del clúster de EKS.

Una vez que se haya establecido la conexión del cliente, se pueden crear y ejecutar tareas de Dask en el clúster de EKS utilizando el Dask Client.

## Conectar por medio de una url a un cluster remoto

1. Crear un clúster de EKS: Para crear un clúster de EKS, se puede utilizar la consola de AWS o la herramienta de línea de comandos eksctl. Asegúrese de que el clúster tenga nodos suficientes para ejecutar el programador y los trabajadores de Dask.

2. Instalar Helm en el clúster de EKS: Helm es una herramienta que permite instalar y gestionar aplicaciones en Kubernetes. Para instalar Helm en el clúster de EKS, se puede seguir la guía oficial de Helm: https://helm.sh/docs/intro/install/.

3. Instalar el chart de Dask en el clúster de EKS: El chart de Dask es una plantilla de Helm que permite instalar y configurar un clúster de Dask en Kubernetes. Para instalar el chart de Dask, se pueden seguir los siguientes pasos:

    a. Agregar el repositorio de Helm de Dask:
        
    ```python
        helm repo add dask https://helm.dask.org/
    ```
    b. Instalar el chart de Dask:
    ```python
        helm install dask dask/dask
    ```

    Esto instalará un programador y un trabajador de Dask en el clúster de EKS.
4. Conectarse al clúster de Dask: Una vez que se ha instalado el clúster de Dask en EKS, se puede conectar al programador utilizando una URL. Para obtener la URL, se puede ejecutar el siguiente comando en la línea de comandos:

```bash
    kubectl port-forward svc/dask-scheduler 8786:8786
```

Esto redirigirá el puerto 8786 del programador al puerto 8786 de la máquina local. A continuación, se puede conectar al clúster de Dask utilizando la siguiente línea de código en Python:

```python
    from dask.distributed import Client

    client = Client("tcp://localhost:8786")
```

Si se desea conectar desde una máquina remota, se debe utilizar la dirección IP o el nombre de dominio de la máquina que ejecuta el programador en lugar de localhost.

Una vez que se ha conectado al clúster de Dask utilizando el Dask Client, se pueden crear y ejecutar tareas de Dask en el clúster.



