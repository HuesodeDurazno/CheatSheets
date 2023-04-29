
## Que es 

HDFS significa Hadoop Distributed File System y es un sistema de archivos distribuido diseñado para almacenar grandes conjuntos de datos de manera confiable y escalable en clústeres de servidores. HDFS forma parte del ecosistema de Hadoop y es una de las principales herramientas utilizadas para el procesamiento distribuido de datos.

HDFS divide los archivos en bloques y los almacena en varios nodos del clúster de servidores, lo que permite una mayor tolerancia a fallos y una alta disponibilidad de los datos. Además, HDFS tiene una arquitectura maestro/esclavo, en la que un nodo maestro (NameNode) administra el sistema de archivos y varios nodos esclavos (DataNodes) almacenan y recuperan los bloques de datos.

En resumen, HDFS es una herramienta clave en el procesamiento de datos distribuidos y es ampliamente utilizada en aplicaciones de big data y análisis de datos.

## Componentes

Los principales componentes de HDFS son los siguientes:

NameNode: Es el nodo maestro del clúster HDFS que gestiona el espacio de nombres del sistema de archivos y mantiene el registro de la ubicación física de cada bloque de datos. El NameNode también se encarga de la administración de permisos de acceso y de la replicación de los bloques de datos para asegurar su disponibilidad y durabilidad.

DataNode: Es un nodo esclavo del clúster HDFS que almacena los bloques de datos. Cada DataNode se comunica regularmente con el NameNode para informar sobre la disponibilidad de los bloques y para solicitar instrucciones sobre su manejo.

Secondary NameNode: Es un nodo secundario que realiza tareas de mantenimiento y respaldo del NameNode. Aunque su nombre pueda inducir a error, el Secondary NameNode no es una copia de seguridad en tiempo real del NameNode, sino que realiza ciertas operaciones periódicas de mantenimiento, como la fusión de archivos de registro de transacciones.

Clientes HDFS: Son las aplicaciones que acceden al sistema de archivos HDFS para leer o escribir datos. Los clientes pueden ser aplicaciones de procesamiento de datos, herramientas de administración o usuarios finales que utilizan una interfaz de línea de comandos.

En resumen, el NameNode y los DataNodes son los componentes principales del sistema de archivos HDFS y son los encargados de garantizar la disponibilidad, durabilidad y escalabilidad del almacenamiento de datos. El Secondary NameNode y los clientes HDFS son componentes secundarios que contribuyen al mantenimiento y al uso del sistema.

## Comandos mas ocupados en hdfs

hdfs dfs -ls [ruta]: Muestra el contenido de un directorio o archivo en la ruta especificada.

hdfs dfs -mkdir [ruta]: Crea un nuevo directorio en la ruta especificada.

hdfs dfs -put [archivo_local] [ruta_hdfs]: Copia un archivo local al sistema de archivos HDFS en la ruta especificada.

hdfs dfs -get [ruta_hdfs] [archivo_local]: Copia un archivo desde el sistema de archivos HDFS a un archivo local.

hdfs dfs -rm [ruta]: Elimina un archivo o directorio en la ruta especificada.

hdfs dfs -mv [ruta_origen] [ruta_destino]: Mueve un archivo o directorio de una ruta a otra en el sistema de archivos HDFS.

hdfs dfs -chown [usuario]:[grupo] [ruta]: Cambia el propietario y el grupo de un archivo o directorio en la ruta especificada.

hdfs dfs -chmod [permisos] [ruta]: Cambia los permisos de un archivo o directorio en la ruta especificada.

hdfs dfsadmin -report: Muestra un informe del estado del clúster HDFS.

hdfs dfs -du [ruta]: Muestra el tamaño en bytes de los archivos en la ruta especificada.

hdfs dfs -cat [ruta]: Muestra el contenido de un archivo en la ruta especificada.

hdfs dfs -tail [ruta]: Muestra las últimas líneas de un archivo en la ruta especificada.

hdfs dfs -count [ruta]: Cuenta el número de archivos, directorios y bytes en la ruta especificada.

hdfs dfs -setrep -R [replicas] [ruta]: Cambia la replicación de los archivos en la ruta especificada.

hdfs dfs -getmerge [ruta_hdfs] [archivo_local]: Combina todos los archivos en la ruta especificada en un solo archivo local.

hdfs dfs -setfacl -R -m [acl] [ruta]: Cambia los permisos de acceso de control de lista (ACL) de un archivo o directorio en la ruta especificada.

hdfs dfs -du -s -h [ruta]: Muestra el tamaño en un formato legible para humanos (por ejemplo, "1.2 GB") de los archivos en la ruta especificada.

Estos son solo algunos ejemplos de los comandos disponibles en HDFS. Hay muchos más comandos y opciones disponibles, dependiendo de las necesidades específicas de tu aplicación.
