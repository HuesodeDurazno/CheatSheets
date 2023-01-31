# dask.delayed

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