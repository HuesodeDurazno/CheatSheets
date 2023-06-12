# Primeros pasos 


## Crear una sesion
```python

from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_training')\
        .getOrCreate()
```

El spark session es el primer paso que debemos de seguir pasra trabajar con spark.

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

5. reduceByKey(): La transformación reduceByKey() combina los valores de un RDD que tienen la misma clave mediante una función de reducción, como la suma o el promedio. Esta transformación se utiliza con frecuencia en operaciones de agregación. Por ejemplo:

```python
# Creamos un RDD de pares clave-valor
rdd = sc.parallelize([(1, 2), (3, 4), (3, 6)])

# Sumamos los valores que tienen la misma clave
new_rdd = rdd.reduceByKey(lambda x, y: x + y)

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: [(1, 2), (3, 10)]
```
6. sortByKey(): La transformación sortByKey() ordena los elementos de un RDD por la clave. Por defecto, los elementos se ordenan de forma ascendente, pero se puede especificar el parámetro ascending=False para ordenarlos de forma descendente. Por ejemplo:

```python
# Creamos un RDD de pares clave-valor
rdd = sc.parallelize([(3, 'a'), (1, 'b'), (2, 'c')])

# Ordenamos los elementos por la clave
new_rdd = rdd.sortByKey()

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: [(1, 'b'), (2, 'c'), (3, 'a')]

```

7. groupByKey(): La transformación groupByKey() agrupa los elementos de un RDD por la clave y devuelve un RDD de pares clave-valor, donde la clave es la clave de agrupación y el valor es un iterable con los valores correspondientes a esa clave. Por ejemplo:

```python
# Creamos un RDD de pares clave-valor
rdd = sc.parallelize([(1, 2), (3, 4), (3, 6)])

# Agrupamos los valores por la clave
new_rdd = rdd.groupByKey()

# Mostramos los elementos del nuevo RDD
for key, value in new_rdd.collect():
    print(f'Clave: {key}, Valor: {list(value)}')
# Output:
# Clave: 1, Valor: [2]
# Clave: 3, Valor: [4, 6]

```

8. sortBy(): La transformación sortBy() ordena los elementos de un RDD según una función de clasificación. La función toma como entrada un elemento del RDD y devuelve un valor que se utiliza para la clasificación. Por ejemplo:

```python
# Creamos un RDD de números
rdd = sc.parallelize([3, 1, 4, 1, 5, 9, 2, 6, 5])

# Ordenamos los elementos por su valor
new_rdd = rdd.sortBy(lambda x: x)

# Mostramos los elementos del nuevo RDD
print(new_rdd.collect())  # Output: [1, 1

```

## Acciones basicas

1. collect(): La acción collect() devuelve todos los elementos de un RDD como una lista de Python en el programa de control. Si el RDD es muy grande, esto puede provocar un desbordamiento de memoria. Por ejemplo:

```python
# Creamos un RDD de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Devolvemos los elementos del RDD como una lista
result = rdd.collect()

# Mostramos el resultado
print(result)  # Output: [1, 2, 3, 4, 5]

```

2. count(): La acción count() devuelve el número de elementos en un RDD. Por ejemplo:

```python
# Creamos un RDD de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Contamos el número de elementos
result = rdd.count()

# Mostramos el resultado
print(result)  # Output: 5

```

3. take(): La acción take() devuelve los primeros n elementos de un RDD como una lista de Python en el programa de control. Si el RDD es muy grande, esto puede provocar un desbordamiento de memoria. Por ejemplo:

```python
# Creamos un RDD de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Devolvemos los dos primeros elementos del RDD como una lista
result = rdd.take(2)

# Mostramos el resultado
print(result)  # Output: [1, 2]

```

4. first(): La acción first() devuelve el primer elemento de un RDD. Por ejemplo:


```python
# Creamos un RDD de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Devolvemos el primer elemento del RDD
result = rdd.first()

# Mostramos el resultado
print(result)  # Output: 1


```

5.reduce(): La acción reduce() combina los elementos de un RDD mediante una función de reducción, como la suma o el promedio. La función reduce() toma como entrada una función de dos argumentos que toma dos elementos del RDD y devuelve un nuevo elemento. Por ejemplo:

```python
# Creamos un RDD de números
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Sumamos los elementos del RDD
result = rdd.reduce(lambda x, y: x + y)

# Mostramos el resultado
print(result)  # Output: 15

```

6. Crear un rdd vacio

```python
rdd= sc.emptyRDD()
```

7. Crear un rdd de un archivo de texto

```python
    rdd = sc.textFile('')
    
    rdd = sc.wholeTextFile('')
```