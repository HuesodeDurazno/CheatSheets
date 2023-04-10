## Que es

Dask DataFrame proporciona una interfaz similar a Pandas DataFrame, lo que hace que sea fácil para los usuarios de Pandas utilizar Dask DataFrame para manejar conjuntos de datos más grandes que no caben en la memoria de una sola máquina. Dask DataFrame puede leer y escribir datos desde una variedad de formatos de datos comunes, incluyendo CSV, Excel, HDF5, Parquet y SQL.

Dask DataFrame divide los datos en bloques de tamaño fijo llamados "particiones". Cada partición se procesa en paralelo en una máquina o proceso separado. Las operaciones de Dask DataFrame se construyen como un gráfico acíclico dirigido (DAG) que representa las dependencias entre las operaciones y las particiones de datos. Dask DataFrame utiliza la planificación de tareas para ejecutar estas operaciones de manera eficiente, minimizando la comunicación y el movimiento de datos entre las particiones.

En resumen, Dask DataFrame es una extensión de Pandas DataFrame que permite el procesamiento de datos en paralelo en múltiples procesos o máquinas, lo que facilita el manejo de grandes conjuntos de datos que no caben en la memoria de una sola máquina.

## funciones importantes

dask.dataframe.read_csv(): esta función permite leer archivos CSV y crear un objeto Dask DataFrame.

```python
    import dask.dataframe as dd

    # Leer un archivo CSV
    df = dd.read_csv('ventas.csv')
```

dask.dataframe.to_csv(): esta función permite guardar un objeto Dask DataFrame en un archivo CSV.
```python
    # Guardar un objeto Dask DataFrame en un archivo CSV
    df.to_csv('ventas_filtradas.csv', index=False)
```

dask.dataframe.head(): esta función muestra las primeras filas del objeto Dask DataFrame.
```python
    # Mostrar las primeras 5 filas del objeto Dask DataFrame
    df.head()
```

dask.dataframe.tail(): esta función muestra las últimas filas del objeto Dask DataFrame.
```python
    # Mostrar las últimas 5 filas del objeto Dask DataFrame
    df.tail()
```

dask.dataframe.groupby(): esta función agrupa los datos según una o varias columnas y permite realizar operaciones de agregación en cada grupo.

```python
    # Agrupar los datos por la columna "producto"
    grupo_producto = df.groupby('producto')

    # Calcular la suma de las ventas por producto
    suma_ventas = grupo_producto['ventas'].sum()
```

dask.dataframe.merge(): esta función permite combinar dos o más objetos Dask DataFrame en función de una o varias columnas comunes.

```python
    # Crear un objeto Dask DataFrame con información de los productos
    df_productos = dd.read_csv('productos.csv')

    # Combinar los objetos Dask DataFrame "ventas" y "productos"
    df_completo = dd.merge(df, df_productos, on='producto')
```

dask.dataframe.drop_duplicates(): esta función elimina las filas duplicadas del objeto Dask DataFrame.

```python
    # Eliminar las filas duplicadas del objeto Dask DataFrame
    df_sin_duplicados = df.drop_duplicates()
```

dask.dataframe.map_partitions(): esta función aplica una función a cada partición del objeto Dask DataFrame.

```python
    # Definir una función para aplicar a cada partición del objeto Dask DataFrame
    def calcular_promedio(particion):
        return particion.mean()

    # Aplicar la función a cada partición del objeto Dask DataFrame
    df_promedio = df.map_partitions(calcular_promedio)
```

dask.dataframe.categorize(): esta función convierte una columna del objeto Dask DataFrame en una categoría.

```python
    # Convertir la columna "categoria" en una categoría
    df['categoria'] = df['categoria'].categorize()
```

dask.dataframe.compute(): esta función procesa los datos del objeto Dask DataFrame y devuelve un objeto Pandas DataFrame.

```python
    # Procesar los datos del objeto Dask DataFrame y convertirlos en un objeto Pandas DataFrame
    df_pandas = df.compute()
```

## Particionar un dask df

En Dask DataFrame, la partición de datos se realiza de manera automática, en función del tamaño de los datos y de la cantidad de memoria disponible en el sistema. Sin embargo, es posible especificar el tamaño máximo de las particiones a través del parámetro chunksize de la función read_csv(), que se utiliza para leer un archivo CSV y crear un objeto Dask DataFrame.

Por ejemplo, para leer un archivo CSV y crear un objeto Dask DataFrame con particiones de 100 MB de tamaño, se puede utilizar el siguiente código:

```python
    import dask.dataframe as dd

    # Leer un archivo CSV y crear un objeto Dask DataFrame con particiones de 100 MB de tamaño
    df = dd.read_csv('archivo.csv', chunksize=100000000)

```

Es importante tener en cuenta que el tamaño de las particiones puede afectar el rendimiento de las operaciones en Dask DataFrame. Por lo tanto, es recomendable ajustar el tamaño de las particiones en función de las características del conjunto de datos y de las capacidades del sistema.

## Crear un dask dataframe con un dask future

Para crear un Dask DataFrame a partir de un Dask Future, primero debemos esperar a que el futuro se complete y devuelva los datos. Una vez que los datos estén disponibles, podemos utilizar la función from_delayed() de Dask DataFrame para crear un objeto Dask DataFrame a partir de una lista de objetos delayed() que representan cada una de las columnas del DataFrame.

Supongamos que tenemos un conjunto de datos que se encuentra en un servidor remoto y que podemos acceder a través de una función que devuelve un futuro. En este ejemplo, utilizaremos la función fetch_data() para obtener un futuro que contiene los datos del DataFrame:

```python
    from dask.distributed import Client
    import dask.dataframe as dd

    client = Client("tcp://localhost:8786") # Conectar al cluster de Dask

    def fetch_data():
        # Código para obtener los datos del DataFrame desde un servidor remoto
        # y devolverlos como una lista de diccionarios
        return data

    # Obtener un futuro que contiene los datos del DataFrame
    future_data = client.submit(fetch_data)
```

Una vez que tengamos el futuro future_data, podemos esperar a que se complete y devuelva los datos utilizando la función result():

```python
    # Esperar a que el futuro se complete y devuelva los datos
    data = future_data.result()
```

A continuación, podemos utilizar la función delayed() de Dask para crear una lista de objetos delayed() que representan cada una de las columnas del DataFrame:

```python
    from dask import delayed

    # Crear una lista de objetos delayed que representan cada una de las columnas del DataFrame
    delayed_data = [delayed(data[column]) for column in data.columns]
```

Finalmente, podemos utilizar la función from_delayed() de Dask DataFrame para crear un objeto Dask DataFrame a partir de la lista de objetos delayed():

```python
    # Crear un objeto Dask DataFrame a partir de la lista de objetos delayed
    df = dd.from_delayed(delayed_data)
```