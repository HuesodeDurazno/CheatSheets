# dask.delayed

sirve para paralelizar codigo existente de python , retorna un lazy delayed object 


## sintaxis de delayed

```python
    from dask import delayed, compute
    res1 = delayed(function)(param1,param2)
    res1.compute()

    or 

    @delayed
```



