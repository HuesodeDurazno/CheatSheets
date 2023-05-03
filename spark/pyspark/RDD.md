# Que es 


RDD significa "Resilient Distributed Dataset" y es una estructura de datos fundamental en la programación distribuida de Apache Spark.

Las características principales de un RDD son las siguientes:

1. Resiliente: significa que un RDD puede recuperarse de fallos o errores. Si un nodo falla, los datos se pueden reconstruir a partir de otros nodos en el clúster.

2. Distribuido: los datos se distribuyen en múltiples nodos en un clúster de computadoras. Esto permite que las operaciones de procesamiento de datos se realicen en paralelo en diferentes nodos.

3. Inmutable: los RDD son inmutables, lo que significa que no se pueden modificar una vez creados. Si es necesario realizar una operación en los datos, se crea un nuevo RDD.

4. Tipado: cada elemento de un RDD tiene un tipo de datos definido. Esto permite que las operaciones en los datos se realicen de manera más eficiente y segura.

5. Lazy evaluation: las transformaciones en los RDD no se ejecutan inmediatamente, sino que se aplazan hasta que se realiza una acción. Esto permite que Spark optimice la ejecución de las operaciones y reduzca el costo de la computación.

6. Soporte para múltiples lenguajes: los RDD son compatibles con varios lenguajes de programación, incluidos Java, Python y Scala.

## Operaciones sobre RDD 

Sobre un RDD se pueden llevar a cabo diversas operaciones, las cuales se pueden clasificar en dos tipos:

1. Transformaciones: Las transformaciones en un RDD son operaciones que generan un nuevo RDD a partir de uno existente. Los RDD son inmutables, por lo que las transformaciones no modifican el RDD original, sino que generan un nuevo RDD con los datos transformados. Algunas transformaciones comunes son:

* map(): Aplica una función a cada elemento del RDD y devuelve un nuevo RDD con los resultados.
* filter(): Selecciona los elementos del RDD que cumplen una determinada condición y devuelve un nuevo RDD con estos elementos.
* flatMap(): Similar a map(), pero permite que la función devuelva múltiples elementos, los cuales se agregan al nuevo RDD como elementos separados.
* groupBy(): Agrupa los elementos del RDD en base a una determinada clave y devuelve un RDD de pares clave-valor, donde la clave es la clave de agrupación y el valor es un iterable con los elementos del grupo.

2. Acciones: Las acciones en un RDD son operaciones que retornan un valor al programa principal o escriben datos a un sistema de almacenamiento externo. Algunas acciones comunes son:
* collect(): Devuelve todos los elementos del RDD al programa principal como una lista de Python.
* count(): Devuelve el número de elementos en el RDD.
* reduce(): Combina los elementos del RDD utilizando una función y devuelve el resultado.
* saveAsTextFile(): Escribe los elementos del RDD en un archivo de texto en un sistema de archivos externo.

Es importante tener en cuenta que las transformaciones son perezosas (lazy), lo que significa que no se ejecutan inmediatamente al ser llamadas, sino que se almacenan en el grafo de ejecución de Spark. Las acciones, en cambio, son operaciones que provocan la ejecución de todas las transformaciones anteriores en el grafo de ejecución.