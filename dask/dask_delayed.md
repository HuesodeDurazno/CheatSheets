# dask.delayed

La idea detrás de Dask Delayed es que, en lugar de ejecutar una función de manera inmediata, se aplaza su ejecución hasta que sea necesario y se combinan varias operaciones en una gráfica de cómputo dirigido. De esta manera, Dask Delayed puede optimizar la ejecución de estas operaciones y ejecutarlas en paralelo para obtener un mejor rendimiento.

sirve para paralelizar codigo existente de python , retorna un lazy delayed object , aplaza la ejecucion y coloca la funcion y sus argumentos en un grafico de tareas.

los schedulers de dask explotarán este paralelismo, generalmente mejorando el rendimiento.
## sintaxis de delayed

```python
    from dask import delayed, compute
    res1 = delayed(function)(param1,param2)
    res1.compute()

    or 

    @delayed
```
# buenas practicas de delayed
Consulta las buenas practicas de dask delayed en https://docs.dask.org/en/stable/delayed-best-practices.html

## Ejemplos
```python
    def inc(x):
        return x + 1

    data = [1, 2, 3, 4, 5]
    result = [inc(x) for x in data]
```

Esta es una forma sencilla de aplicar la función a cada elemento de la lista, pero ¿qué pasa si queremos aplicar varias funciones a los mismos datos y combinar los resultados? Esto puede ser más complicado de hacer con una comprensión de lista simple.

En cambio, podemos utilizar Dask Delayed para aplazar la ejecución de estas operaciones y combinarlas en una gráfica de cómputo. Primero, debemos importar la función delayed de Dask:

```python
    from dask import delayed
    inc_delayed = delayed(inc)
```

En este punto, inc_delayed es una función retrasada que representa la función inc. Podemos utilizar esta función retrasada para construir nuestra gráfica de cómputo. Por ejemplo, podemos aplicar la función a cada elemento de la lista y combinar los resultados utilizando la función sum:

```python

    results = []
    for x in data:
        y = inc_delayed(x)
        z = inc_delayed(y)
        w = inc_delayed(z)
        results.append(w)

    final_result = delayed(sum)(results)
```

En este ejemplo, estamos aplicando la función inc_delayed a cada elemento de la lista data y almacenando los resultados en la lista results. Luego, estamos combinando los resultados utilizando la función sum. Sin embargo, en lugar de llamar directamente a sum, estamos utilizando la función delayed para retrasar su ejecución hasta que sea necesario.

Una vez que hemos construido nuestra gráfica de cómputo, podemos ejecutarla utilizando la función compute:

```python
    final_result.compute()
```

Además, podemos utilizar la función visualize() para generar un gráfico del grafo de tareas que representa la computación a realizar. Este gráfico puede ser útil para entender mejor la estructura de la computación y encontrar posibles cuellos de botella o puntos de optimización.

```python
    import dask
    from dask import delayed

    @delayed
    def add(a, b):
        return a + b

    @delayed
    def square(a):
        return a ** 2

    @delayed
    def neg(a):
        return -a

    x = add(1, 2)
    y = add(x, 3)
    z = square(y)
    w = neg(z)

    result = w.compute()
    dask.visualize(w)
```

