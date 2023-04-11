## que es

En Python, podemos implementar iteradores personalizados en nuestras clases utilizando los métodos especiales __iter__ y __next__. Estos métodos permiten que nuestras clases sean utilizadas en un contexto iterable, lo que significa que podemos utilizarlas en un bucle for o con la función next() para iterar sobre los elementos de la instancia de la clase.

El método __iter__ debe devolver un objeto que tenga un método __next__. El método __next__ devuelve el siguiente elemento de la secuencia y genera una excepción StopIteration cuando se alcanza el final de la secuencia.

## Ejemplo 

```python
    class Contador:
        def __init__(self, limite):
            self.limite = limite
            self.valor = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.valor >= self.limite:
                raise StopIteration
            self.valor += 1
            return self.valor - 1

```

Podemos utilizar esta clase en un bucle for para iterar sobre los valores del contador:

```python
    c = Contador(5)
    for valor in c:
        print(valor)
```

También podemos utilizar la función next() para obtener el siguiente valor del contador:

```python
    c = Contador(3)
    print(next(c))  # 0
    print(next(c))  # 1
    print(next(c))  # 2
    print(next(c))  # Genera StopIteration

```