# Primeros pasos 


## Crear una sesion
```python

from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_training')\
        .getOrCreate()
```

El spark session es el primer paso que debemos de seguir pasra trabajar copn spark.

Al metodo master le pasamos el modo como se va a ejecutar pyspark , en este caso local el numero dentro de [] indica el numero de particiones en los rdd , dataframes o datasets

app name agrega el nombre de la aplicacion

getorCreate se utiliza para obtener una spark session o obtener una ya existente.

El spark session crea internamente el spark config y spark context 


Version resumida:

```python
spark = SparkSession.builder.getOrCreate()
```

Despues de tener nuestra Sparksession tenemos que obtener nuestro sparkContext con

```python
    sc = spark.sparkContext
```

## Transformaciones basicas

1. map(): La transformación map() aplica una función a cada elemento del RDD y devuelve un nuevo RDD con los resultados. Por ejemplo:

```python
# Creamos un RDD con una lista de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Aplicamos la función lambda a cada elemento del RDD
new_rdd = rdd.map(lambda x: x * 2)

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: [2, 4, 6, 8, 10]

```

2. filter(): La transformación filter() selecciona los elementos del RDD que cumplen una determinada condición y devuelve un nuevo RDD con estos elementos. Por ejemplo:

```python
# Creamos un RDD con una lista de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Seleccionamos los elementos pares del RDD
new_rdd = rdd.filter(lambda x: x % 2 == 0)

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: [2, 4]

```

3. flatMap(): La transformación flatMap() es similar a map(), pero permite que la función devuelva múltiples elementos, los cuales se agregan al nuevo RDD como elementos separados. Por ejemplo:

```python
# Creamos un RDD con una lista de strings
rdd = sc.parallelize(['hola mundo', 'adios mundo'])

# Aplicamos la función lambda para obtener las palabras de cada string
new_rdd = rdd.flatMap(lambda x: x.split(' '))

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: ['hola', 'mundo', 'adios', 'mundo']

```

4. groupBy(): La transformación groupBy() agrupa los elementos del RDD en base a una determinada clave y devuelve un RDD de pares clave-valor, donde la clave es la clave de agrupación y el valor es un iterable con los elementos del grupo. Por ejemplo:

```python
# Creamos un RDD con una lista de strings
rdd = sc.parallelize(['hola', 'adios', 'buenos', 'dias'])

# Agrupamos los strings por la primera letra
new_rdd = rdd.groupBy(lambda x: x[0])

# Mostramos los elementos del nuevo RDD
for key, value in new_rdd.collect():
    print(f'Clave: {key}, Valor: {list(value)}')
# Output:
# Clave: h, Valor: ['hola']
# Clave: a, Valor: ['adios']
# Clave: b, Valor: ['buenos']
# Clave: d, Valor: ['dias']

```