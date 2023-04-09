# Introduccion a dask

Al tratar con grandes volumenes de informacion, en algun momento esta informacion debera ser gestionada por la memoria RAM , en algunas ocaciones no podremos cargar en memoria tanta informacion

## dask como una solucion

Es una solucion de computo distribuido , nos permite trabajar con multiples cores.

Tiene una sintaxis muy similar a librerias muy conocidas como pandas o numpy

Distribuye nuestras tareas en pequeños batchs y los computa atravez de un task scheduler y un task worker

Hay herramientas parecidas como pyspark , pero dask es mas facil de migrar

## Que es el cluster computing 

Es el proceso de usar una o una serie de computadoras conectadas por una red rapida, trabajan juntas en forma paralela para formar un solo recurso computacional. (una computadora hecha de mas computadoras)

![example_cluster](./imgs/example_cluster.PNG)

## tipos de dask schedulers

1. Single Machine
2. Distributed scheduler

![dask_scheduler](./imgs/dask_scheduler.PNG)

El scheduler distribuido te permite ingresar a un dashboard en el puerto 8787 cuando el cluster se inicializa

## iniciar un cluster e inciar el clientes

```python

from dask.distributed import LocalCluster, Client
cluster = LocalCluster()
client = Client(cluster)
#To see where the port of the dashboard is, use this command
print(client.scheduler_info()['services'])
# {'dashboard': 8787} --> means you can access it at localhost:8787
```

## como trabaja dask a alto nivel

Supongamos que tenemos un conjunto de datos muy grande, como el conjunto de datos de las ventas de una tienda durante varios años. Si queremos calcular la suma total de todas las ventas, no podríamos hacerlo directamente con pandas (otra librería de Python para trabajar con datos) porque no cabría en la memoria RAM. Pero con Dask, podemos dividir el conjunto de datos en pequeñas partes, cada una de ellas lo suficientemente pequeña para caber en la memoria RAM. A continuación, podemos calcular la suma de cada parte de forma paralela y, finalmente, sumar todas las sumas parciales para obtener la suma total.

un array o un dataframe en dask se compone de chunks de df pandas o arrays numpy

![high_level_arrays](./imgs/high_level_array.PNG)
![high_level_pandas](./imgs/high_level_pandas.PNG)

Además, Dask también nos permite trabajar con datos en paralelo en disco, lo que significa que podemos procesar grandes conjuntos de datos que están almacenados en disco sin tener que cargar todo el conjunto de datos en la memoria RAM. Esto es especialmente útil cuando se trabaja con conjuntos de datos que son demasiado grandes para almacenar en la memoria RAM de cualquier máquina.

## Como se organizan las tareas y se crea un grafo

En Dask, el procesamiento se divide en pequeñas tareas y se ejecutan en paralelo en múltiples procesos o máquinas. Las tareas se organizan en un grafo de dependencias, en el que cada tarea depende de las tareas que la preceden.

Para generar un grafo en Dask, se siguen los siguientes pasos:

1. Se define una operación a realizar en los datos. Por ejemplo, podemos querer leer un archivo CSV o aplicar una función a los datos.

2. Dask crea una "tarea" para cada operación definida. Estas tareas se agrupan en "grupos de tareas" lógicas. Por ejemplo, todas las tareas relacionadas con la lectura de un archivo CSV se agruparán en un grupo de tareas.

3. Dask analiza las dependencias entre las tareas. Si una tarea depende de otra tarea, se agrega una flecha entre las tareas en el grafo. Por ejemplo, si queremos aplicar una función a los datos después de leerlos de un archivo CSV, la tarea de aplicación de función dependerá de la tarea de lectura de archivo.

4. Dask optimiza el grafo para reducir el tiempo de ejecución. Esto implica reordenar las tareas para minimizar los cuellos de botella y maximizar el uso de los recursos.n Dask, el procesamiento se divide en pequeñas tareas y se ejecutan en paralelo en múltiples procesos o máquinas. Las tareas se organizan en un grafo de dependencias, en el que cada tarea depende de las tareas que la preceden.

Para visualizar el grafo podemos ocupar:

    dask.visualize