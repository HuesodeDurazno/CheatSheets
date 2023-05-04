Para empezar a trabajar con dataframes tenemosd que crear una spark session

 ## Operaciones comunes 

 1. count(): La operación count() se utiliza para contar el número de filas en un DF. Por ejemplo:

 ```python
 # Contamos el número de filas en el DF
df.count()
 ```

 2. columns: La propiedad columns se utiliza para obtener una lista de las columnas en un DF. Por ejemplo:

 ```python
 # Obtenemos una lista de las columnas en el DF
df.columns

 ```
3. dtypes: La propiedad dtypes se utiliza para obtener una lista de las columnas en un DF junto con sus tipos de datos. Por ejemplo:

```python
# Obtenemos una lista de las columnas en el DF junto con sus tipos de datos
df.dtypes
```

4. printSchema(): La operación printSchema() se utiliza para imprimir el esquema de un DF. El esquema muestra las columnas del DF junto con sus tipos de datos y si permiten nulos o no. Por ejemplo:

```python
# Imprimimos el esquema del DF
df.printSchema()
```

5. select(): La operación select() se utiliza para seleccionar columnas de un DF. Puede usarse para seleccionar una o varias columnas del DF. Por ejemplo:
```python
# Seleccionamos las columnas 'nombre' y 'edad'
df.select('nombre', 'edad')
```

6. La operación filter() en PySpark se utiliza para filtrar filas de un DataFrame (DF) en función de una condición. La condición puede ser una expresión booleana o una columna que contenga valores booleanos.

```python
# Filtramos las filas donde la edad es mayor que 25
df.filter(df.edad > 25)
# Filtramos las filas donde la columna "casado" es verdadera
df.filter(df.casado == True)
# Filtramos las filas donde el nombre empieza por "J" y la edad es mayor que 25
df.filter((df.nombre.startswith('J')) & (df.edad > 25))

```

7. drop(): La operación drop() se utiliza para eliminar una o varias columnas de un DF. Por ejemplo:

```python
# Eliminamos la columna 'apellido' del DF
df.drop('apellido')
```

8. groupBy(): La operación groupBy() se utiliza para agrupar filas de un DF por una o varias columnas y realizar cálculos en cada grupo. Por ejemplo:

```python

# Agrupamos por la columna "grupo" y aplicamos algunas funciones de agregación
df.groupBy('grupo').agg({'puntos': 'sum', 'id': 'count', 'puntos': 'avg'}).show()

# Agrupar por multiples columnas
df.groupBy(['grupo', 'nombre']).agg({'puntos': 'sum'}).show()

#Especificar nombres de columnas personalizados para las funciones de agregación:
from pyspark.sql.functions import sum as spark_sum

df.groupBy('grupo').agg(spark_sum('puntos').alias('puntos_totales')).show()



```

9. sort(): La operación sort() se utiliza para ordenar filas de un DF en función de una o varias columnas. Por ejemplo:

```python
#Ordenar por una columna en orden ascendente:
df.sort('edad').show()
#Ordenar por múltiples columnas en orden ascendente:
df.sort(['grupo', 'puntos']).show()
#Ordenar por una columna en orden descendente:
df.sort('edad', ascending=False).show()
#Ordenar por múltiples columnas en orden descendente:
df.sort(['grupo', 'puntos'], ascending=[False, False]).show()

```

10. withColumn(): La operación withColumn() se utiliza para añadir una nueva columna a un DF o reemplazar una existente. La nueva columna se crea a partir de una expresión o función que utiliza una o varias columnas existentes del DF. Por ejemplo:

```python
# Añadimos una nueva columna 'edad_doble' que contiene el doble de la edad
df.withColumn('edad_doble', df.edad * 2)
```

## Joins

En PySpark, hay cuatro tipos de operaciones de join que se utilizan para combinar dos DataFrames: inner, outer, left y right. Cada tipo de join es adecuado para una tarea específica.

1. inner join: Este tipo de join devuelve los registros comunes que se encuentran en ambos DataFrames. Es decir, solo se muestran los registros que coinciden en ambas tablas. 

2. outer join: Este tipo de join devuelve todos los registros de ambos DataFrames, incluidos aquellos que no tienen una coincidencia en la otra tabla. Si no hay una coincidencia, se mostrará null para los valores de esa tabla.

3. left join: Este tipo de join devuelve todos los registros del DataFrame de la izquierda y aquellos registros del DataFrame de la derecha que coinciden con los registros del DataFrame de la izquierda.

4. right join: Este tipo de join devuelve todos los registros del DataFrame de la derecha y aquellos registros del DataFrame de la izquierda que coinciden con los registros del DataFrame de la derecha.

Ejemplos :

```python
# DataFrame 1
df1 = spark.createDataFrame([(1, 'John'), (2, 'Jane'), (3, 'Mike')], ['id', 'name'])

# DataFrame 2
df2 = spark.createDataFrame([(1, 'Marketing'), (2, 'Sales'), (4, 'HR')], ['id', 'department'])

```
inner:

```python
# Inner Join
inner_join = df1.join(df2, on=['id'], how='inner')
inner_join.show()

+---+----+----------+
| id|name|department|
+---+----+----------+
|  1|John| Marketing|
|  2|Jane|     Sales|
+---+----+----------+

```
Outer :

```python
# Outer Join
outer_join = df1.join(df2, on=['id'], how='outer')
outer_join.show()


+---+----+----------+
| id|name|department|
+---+----+----------+
|  1|John| Marketing|
|  3|Mike|      null|
|  2|Jane|     Sales|
|  4|null|        HR|
+---+----+----------+

```

left :

```python
# Left Join
left_join = df1.join(df2, on=['id'], how='left')
left_join.show()



+---+----+----------+
| id|name|department|
+---+----+----------+
|  1|John| Marketing|
|  3|Mike|      null|
|  2|Jane|     Sales|
+---+----+----------+


```
Right :
```python
# Right Join
right_join = df1.join(df2, on=['id'], how='right')
right_join.show()

+---+----+----------+
| id|name|department|
+---+----+----------+
|  1|John| Marketing|
|  2|Jane|     Sales|
|  4|null|        HR|
+---+----+----------+

```
Tambien existen Left Outer Join, Right Outer Join   


## SPARK SQL 
Para trabajar con spark sql hace falta crear un temp view 


```python
# Creamos una vista temporal del DataFrame para poder ejecutar consultas SQL
df.createOrReplaceTempView("datos")

# Ejecutamos una consulta SQL sobre la vista temporal
resultados = spark.sql("SELECT COUNT(*) FROM datos WHERE edad >= 18")

# Mostramos los resultados
resultados.show()
```

## Origenes extra

Para leer y escribir un archivo CSV con Spark, puedes utilizar la función read.csv() para cargar el archivo como un DataFrame y la función write.csv() para escribir el DataFrame en un archivo CSV.

```python
from pyspark.sql import SparkSession

# Creamos una instancia de SparkSession
spark = SparkSession.builder.appName("Ejemplo CSV").getOrCreate()

# Leemos un archivo CSV como DataFrame
df = spark.read.csv("datos.csv", header=True, inferSchema=True)

# Mostramos el contenido del DataFrame
df.show()

# Escribimos el DataFrame en un archivo CSV
df.write.csv("resultados.csv", header=True, mode="overwrite")
```