Primero debemos crear la sparkSession

Posteriormente debes crear tablas temporales con los DF a utilizar

## Brodcast join

Broadcast join es una técnica de optimización de Spark que se utiliza para acelerar las operaciones de join cuando uno de los DataFrames involucrados en el join es mucho más pequeño que el otro. En lugar de enviar el DataFrame pequeño a todos los nodos, lo que podría ser costoso en términos de comunicación, se transmite como una variable de broadcast a cada nodo y se realiza el join localmente en cada nodo.

Para utilizar broadcast join en Spark, debes seguir los siguientes pasos:

1. Identifica cuál de los DataFrames involucrados en el join es el más pequeño.

2. Utiliza la función broadcast() para transmitir el DataFrame pequeño como una variable de broadcast:

```python
    from pyspark.sql.functions import broadcast

    df_small = spark.read.csv("small.csv", header=True)
    df_large = spark.read.csv("large.csv", header=True)

    df_joined = df_large.join(broadcast(df_small), "key")

```

En este ejemplo, df_small es el DataFrame pequeño que se transmitirá como una variable de broadcast. Se utiliza la función broadcast() para envolver el DataFrame antes de realizar el join con df_large.

Especifica la columna por la cual se realizará el join. En este ejemplo, utilizamos la columna "key" para realizar el join.

## cache

En Spark, la función cache() se utiliza para almacenar en memoria (o en disco) los datos de un DataFrame o RDD en un momento determinado para que puedan ser reutilizados de manera más eficiente en operaciones futuras.

La función cache() es útil cuando necesitas realizar múltiples operaciones en un mismo DataFrame o RDD. Almacenar los datos en memoria puede reducir significativamente el tiempo de ejecución, ya que los datos no tienen que ser leídos desde el almacenamiento cada vez que se realiza una operación.

La función cache() es fácil de usar, solo tienes que llamarla en el DataFrame o RDD que deseas almacenar en caché:

```python
df = spark.read.csv("data.csv", header=True)

# Cache the DataFrame
df.cache()

```

Ten en cuenta que el almacenamiento en caché de un DataFrame o RDD puede consumir una cantidad significativa de memoria, dependiendo del tamaño de los datos. Además, si los datos cambian frecuentemente o si solo se utilizan una vez, el almacenamiento en caché puede no ser beneficioso en términos de tiempo de ejecución. En esos casos, se puede utilizar la función unpersist() para eliminar los datos de la memoria caché:

```python
# Remove DataFrame from cache
df.unpersist()
```

Es importante tener en cuenta que Spark administra automáticamente la memoria caché y puede eliminar los datos de la memoria caché si se necesita más memoria para otras operaciones. Por lo tanto, no es necesario preocuparse por la administración manual de la memoria caché.

