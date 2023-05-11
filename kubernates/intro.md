# Que es

Kubernetes es una plataforma de orquestación de contenedores de código abierto que automatiza y gestiona la implementación, el escalado y la gestión de aplicaciones en contenedores. Fue desarrollado por Google y ahora es mantenido por la Cloud Native Computing Foundation (CNCF).

Kubernetes permite a los desarrolladores y a los equipos de operaciones automatizar la implementación, la actualización y el escalado de aplicaciones en contenedores en diferentes entornos, como en la nube o en un centro de datos local. Ofrece características avanzadas, como la gestión de recursos, el equilibrio de carga y la gestión de almacenamiento, lo que facilita la creación y la gestión de aplicaciones escalables y altamente disponibles.


# Arquitectura

![arq kubernates](./img/arq_kubernates.png)

1. Master de Kubernetes: El Master es el componente principal de la arquitectura de Kubernetes. Es responsable de la gestión y control del clúster. El Master se compone de varios componentes, como el API Server, el Control Manager, el Scheduler y el Etcd.

2. Nodos: Los Nodos son las máquinas que ejecutan los contenedores y son los componentes que se encargan de la ejecución de las aplicaciones. Cada nodo tiene un agente llamado Kubelet que se comunica con el Master para recibir instrucciones.

3. Pods: Un Pod es la unidad más pequeña en la arquitectura de Kubernetes y se compone de uno o varios contenedores. Cada Pod tiene una dirección IP única y comparte los recursos del Nodo en el que se ejecuta.

4. Servicios: Los Servicios son los componentes que permiten la comunicación entre los Pods. Cada servicio tiene una dirección IP fija y se utiliza para enrutar el tráfico a los Pods correspondientes.

5. Volúmenes: Los Volúmenes son los componentes que permiten el almacenamiento persistente de los datos en Kubernetes. Los Volúmenes se utilizan para asegurar que los datos almacenados en los contenedores se mantengan disponibles incluso si los Pods se eliminan o se reinician.

6. Controladores: Los Controladores son los componentes que se utilizan para asegurar que los objetos en Kubernetes estén en el estado deseado. Por ejemplo, el Controlador de Replicación se utiliza para mantener un número determinado de réplicas de una aplicación en ejecución.



## Objects

En Kubernetes, los objetos son representaciones abstractas de los componentes que forman una aplicación y sus requisitos de recursos. Los objetos de Kubernetes se utilizan para definir el estado deseado de la aplicación, que Kubernetes se encarga de mantener.

Algunos ejemplos de objetos en Kubernetes son los siguientes:

1. Pod: Un Pod es la unidad más pequeña de Kubernetes y representa un contenedor o un grupo de contenedores que se ejecutan juntos en un nodo. Un Pod se utiliza para garantizar que los contenedores se ejecuten en la misma máquina física y compartan recursos.

2. Deployment: Un Deployment se utiliza para definir cómo se debe implementar una aplicación en Kubernetes. Define el número de réplicas que se deben crear y cómo se deben actualizar las réplicas existentes cuando hay un cambio en el estado deseado.

3. Service: Un Service se utiliza para exponer una aplicación en Kubernetes. Permite que los usuarios externos o las aplicaciones se conecten a los Pods que ejecutan la aplicación, incluso si los Pods se mueven a diferentes nodos.

4. ConfigMap: Un ConfigMap se utiliza para almacenar datos de configuración que se utilizan por los contenedores en un Pod.

5. Secret: Un Secret se utiliza para almacenar datos confidenciales como claves de acceso y contraseñas. Los Secret se pueden montar como un volumen en un Pod y los datos se proporcionan como variables de entorno o archivos.

Estos son solo algunos ejemplos de los objetos que se pueden utilizar en Kubernetes. Cada objeto tiene una definición YAML que describe sus propiedades y cómo interactúa con otros objetos en el clúster de Kubernetes.