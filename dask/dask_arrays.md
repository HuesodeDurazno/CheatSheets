## Que son

Dask Arrays es una biblioteca de Python para realizar cálculos numéricos en grandes conjuntos de datos que no caben en la memoria RAM de una sola computadora. Dask Arrays utiliza un enfoque de división de datos en bloques y paralelización de cálculos para trabajar con datos que son demasiado grandes para caber en la memoria de una sola máquina. Los arrays Dask son compatibles con NumPy y se pueden utilizar con las mismas funciones y métodos de NumPy.

Un array Dask se divide en bloques, cada uno de los cuales es un NumPy Array. Estos bloques pueden estar almacenados en la memoria de una sola máquina o distribuidos en un clúster de máquinas. Las operaciones en un array Dask se realizan de forma perezosa, lo que significa que se construye un grafo de dependencias que representa el conjunto de operaciones que se deben realizar. Luego, Dask optimiza y ejecuta este grafo de manera eficiente, utilizando múltiples núcleos de CPU o máquinas para paralelizar la computación.

## Como crear un dask array

Para trabajar con Dask Arrays, necesitas importar el paquete dask.array. A continuación, se muestra un ejemplo de cómo crear un array Dask a partir de un array NumPy existente:

```python
    import numpy as np
    import dask.array as da

    x = np.random.rand(1000000)
    dask_array = da.from_array(x, chunks=1000)
```

El parámetro chunks especifica el tamaño de los bloques en los que se divide el array Dask. En este caso, estamos dividiendo el array en bloques de 1000 elementos cada uno.

podemos realizar diferentes transformaciones sobre este array , para obtener el resultado hacemos uso de la funcion **compute**

## Funciones importantes

da.from_array: convierte un array NumPy en un array Dask

```python
    import numpy as np
    import dask.array as da

    x = np.random.rand(1000000)
    dask_array = da.from_array(x, chunks=1000)
```

da.zeros: crea un array Dask lleno de ceros.

```python
    import dask.array as da

    dask_array = da.zeros((1000, 1000), chunks=(100, 100))
```

da.ones: crea un array Dask lleno de unos.

```
    import dask.array as da

    dask_array = da.ones((1000, 1000), chunks=(100, 100))

```

da.arange: crea un array Dask que contiene una secuencia de valores.

```
    import dask.array as da

    dask_array = da.arange(1000000, chunks=1000)
```

da.random: crea un array Dask con valores aleatorios.

```python

    import dask.array as da

    dask_array = da.random.normal(size=(1000, 1000), chunks=(100, 100))

```

da.sum: calcula la suma de los elementos del array.

```python
    result = dask_array.sum().compute()
```

da.mean: calcula la media de los elementos del array.

```python
    da.mean: calcula la media de los elementos del array.
```

da.std: calcula la desviación estándar de los elementos del array.

```python
    result = dask_array.std().compute()
```

da.dot: realiza una multiplicación de matrices.

```python
    import dask.array as da

    x = da.random.normal(size=(1000, 1000), chunks=(100, 100))
    y = da.random.normal(size=(1000, 1000), chunks=(100, 100))
    result = da.dot(x, y).compute()
```

da.fft.fft: realiza una transformación de Fourier.

```python
    import dask.array as da

    x = da.random.normal(size=(1000, 1000), chunks=(100, 100))
    result = da.fft.fft(x).compute()

```

Hay muchas más funciones disponibles para trabajar con arrays Dask, como da.concatenate, da.transpose, da.reshape, da.convolve, entre otras.

