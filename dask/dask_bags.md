## Dask arrays

En las funciones de dask agregar los chunks

```python
    
    dask_arr = da.random.randint(20,size=20,chunks=3)
    dask_arr.compute()
    #Chunkns tendra el nombre de los chunks que necesitas
```

ver chunks

```python
    dask_arr.chunks
```

visualizar grafico de el proceso

```python
    dask.visualize()
    # para ver de manera horizontal rankdir="LR"
```
