## Que es

Dask Distributed es una biblioteca que permite ejecutar cálculos paralelos y distribuidos en un clúster de máquinas. Es una extensión de Dask que nos permite escalar nuestras computaciones en múltiples nodos, lo que nos permite procesar grandes conjuntos de datos en paralelo.

La idea básica de Dask Distributed es que podemos crear una red de trabajadores (workers) que se comunican entre sí para procesar nuestros cálculos. Cada worker es un proceso de Python que se ejecuta en una máquina separada. Los workers se comunican a través de un scheduler, que coordina la asignación de tareas y la distribución de datos.

Veamos un ejemplo de cómo utilizar Dask Distributed. Primero, debemos iniciar un clúster de trabajadores utilizando la función dask.distributed.Client().

Ejemplo: 

```python
    import dask.array as da

    x = da.random.random((10000, 10000), chunks=(1000, 1000))
    y = x + x.T
    z = y.mean(axis=0)

    result = z.compute()
```

Para ejecutar estos cálculos en paralelo utilizando Dask Distributed, debemos cambiar la última línea de código de z.compute() a client.compute(z). Esto le indica a Dask que queremos ejecutar la tarea z utilizando el clúster de trabajadores que hemos creado.'

Podemos usar la función dashboard_link() del cliente para obtener un enlace al panel de control web de Dask. Este panel nos permite ver en tiempo real el estado de los workers, el progreso de la tarea y otros detalles útiles.

```python
    print(client.dashboard_link())
```

## Principales funciones de dask Distributed

1. Client: El objeto Client es la forma principal de interactuar con un conjunto de trabajadores de cómputo de Dask. El Client se conecta con el conjunto de trabajadores y proporciona una API para enviar tareas a los trabajadores y recuperar resultados.

2. submit: La función submit permite enviar tareas de cómputo a los trabajadores de Dask. La función devuelve un objeto Future que representa el resultado de la tarea. El objeto Future es una promesa de que el resultado estará disponible en algún momento en el futuro.

3. compute: La función compute se utiliza para ejecutar una gráfica de tareas de cómputo en un conjunto de trabajadores de Dask. La función devuelve el resultado de la gráfica de tareas. La función compute utiliza el objeto Client para enviar tareas a los trabajadores y recuperar los resultados.

4. map: La función map permite aplicar una función a múltiples elementos de una colección de datos de manera distribuida. La función devuelve una lista de objetos Future que representan los resultados de la aplicación de la función a cada elemento de la colección.

5. scatter: La función scatter se utiliza para distribuir datos entre los trabajadores de Dask. La función devuelve un objeto Future que representa los datos distribuidos.

6. gather: La función gather se utiliza para recuperar datos distribuidos de los trabajadores de Dask. La función devuelve los datos recuperados.

7. cancel: La función cancel se utiliza para cancelar una tarea que se ha enviado a los trabajadores de Dask. La función toma como argumento el objeto Future que representa la tarea que se desea cancelar.

8. shutdown: La función shutdown se utiliza para apagar los trabajadores de Dask. La función toma como argumento el objeto Client que se utiliza para conectarse con los trabajadores.

## Ejemplos 

```python
from dask.distributed import Client, LocalCluster
import dask.array as da

if __name__ == "__main__":
    # Iniciar un cluster local de Dask Distributed
    cluster = LocalCluster()
    client = Client(cluster)

    # Crear un arreglo Dask distribuido con números aleatorios
    x = da.random.normal(size=(100000, 1000), chunks=(1000, 1000))

    # Enviar el arreglo a los nodos del cluster
    x_scattered = client.scatter(x)

    # Calcular la media y la desviación estándar del arreglo en paralelo
    mean = client.submit(da.mean, x_scattered)
    std = client.submit(da.std, x_scattered)

    # Esperar a que se completen los cálculos y recoger los resultados
    mean_result = client.gather(mean)
    std_result = client.gather(std)

    # Imprimir los resultados
    print("Media: ", mean_result)
    print("Desviación estándar: ", std_result)

    # Cancelar cualquier tarea pendiente
    client.cancel(mean)
    client.cancel(std)

    # Liberar los recursos del cluster
    client.shutdown()

```

En este ejemplo, primero se inicia un cluster local de Dask Distributed y se crea una lista de rangos de números para buscar números primos en paralelo. Luego se envían los cálculos a los nodos del cluster utilizando la función submit, que devuelve un objeto "future" que representa el resultado de la tarea. A continuación, se espera a que se completen todos los cálculos utilizando la función gather, que devuelve una lista con los resultados de todas las tareas. Finalmente, se cancelan todas las tareas pendientes utilizando la función cancel.

```python
from dask.distributed import Client, LocalCluster
import dask.array as da

if __name__ == "__main__":
    # Iniciar un cluster local de Dask Distributed
    cluster = LocalCluster()
    client = Client(cluster)

    # Crear un arreglo Dask distribuido con números aleatorios
    x = da.random.normal(size=(100000, 1000), chunks=(1000, 1000))

    # Enviar el arreglo a los nodos del cluster
    x_scattered = client.scatter(x)

    # Calcular la media y la desviación estándar del arreglo en paralelo
    mean = client.submit(da.mean, x_scattered)
    std = client.submit(da.std, x_scattered)

    # Esperar a que se completen los cálculos y recoger los resultados
    mean_result = client.gather(mean)
    std_result = client.gather(std)

    # Imprimir los resultados
    print("Media: ", mean_result)
    print("Desviación estándar: ", std_result)

    # Cancelar cualquier tarea pendiente
    client.cancel(mean)
    client.cancel(std)

    # Liberar los recursos del cluster
    client.shutdown()

```

En este ejemplo, primero se inicia un cluster local de Dask Distributed y se crea un arreglo Dask distribuido con números aleatorios. Luego se envía el arreglo a los nodos del cluster utilizando la función scatter, que divide el arreglo en bloques y distribuye estos bloques a los nodos del cluster. A continuación, se calcula la media y la desviación estándar del arreglo en paralelo utilizando la función submit, que devuelve un objeto "future" que representa el resultado de la tarea. Se espera a que se completen los cálculos utilizando la función gather, que devuelve los resultados de las tareas. Finalmente, se cancelan todas las tareas pendientes utilizando la función cancel, y se liberan los recursos del cluster utilizando la función shutdown.

