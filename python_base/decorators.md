# Decorators

La funcion de los decoradores es modificar el comportamiento de una clase o funcion, la funcion es usuada como un argumento en otra funcion , depues se llama dentro de una funcion contenedora (wrapper function)

## decorador simple
```python

    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    def say_whee():
        print("Whee!")

    say_whee = my_decorator(say_whee)

``` 

La funcion se pasa como parametro y la referencia sigue existiendo cuando se ejecuta ```wrapper``` la nueva funcion , con un comportamiento distinto se re asigna a la variable say_whee , que  ahora tiene un comportamiento extendido y hace referncia a la funcion my_decorator

## Syntaxis amable

```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")
```

el @ solo es una forma mas facil de escribir ```say_whee = my_decorator(say_whee)```

## pasar argumenos
Se usar args y kwargs

```python
    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            func(*args, **kwargs)
            func(*args, **kwargs)
        return wrapper_do_twice
```

## retornar valores en decorators
Asegurarte de que la wrapper function retorne el valor de la funcion

```python
    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper_do_twice
```

## Introspection

La introspeccion es la habilidad de un objeto de saber sus atributos en tiempo de ejecucion.

Ejemplo: 

```python

    >>> print
    <built-in function print>

    >>> print.__name__
    'print'

    >>> help(print)
    Help on built-in function print in module builtins:

    print(...)
        <full help message>

```

Cuando hacemos uso de introspeccion en una funcion decorada , hara referencia a la funcion wrapper , para evitar esto tenemos que hacer uso de ```@functools.wraps``` , este decorador , perservara la informacion de la funcion original.

```python 

    import functools

    def do_twice(func):
        @functools.wraps(func)
        def wrapper_do_twice(*args, **kwargs):
            func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper_do_twice
```

## Ejemplos de decoradores en la vida real

Timers 
```python
    import functools
    import time

    def timer(func):
        """Print the runtime of the decorated function"""
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()    # 1
            value = func(*args, **kwargs)
            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper_timer

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

```

## Debug code 

Trackeo de los argumentos y salia de una funcion

```python

    import functools
    import time

    def timer(func):
        """Print the runtime of the decorated function"""
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()    # 1
            value = func(*args, **kwargs)
            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper_timer

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])
```

## realentizar codigo

Realentizar n segundos la ejecucion de una funcion

```python
    import functools
    import time

    def slow_down(func):
        """Sleep 1 second before calling the function"""
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(1)
            return func(*args, **kwargs)
        return wrapper_slow_down

    @slow_down
    def countdown(from_number):
        if from_number < 1:
            print("Liftoff!")
        else:
            print(from_number)
            countdown(from_number - 1)
```

# registrar funciones o plugins
Se puede usar para crear un ```light-weight plug-in architecture```.

```python
    import random
    PLUGINS = dict()

    def register(func):
        """Register a function as a plug-in"""
        PLUGINS[func.__name__] = func
        return func

    @register
    def say_hello(name):
        return f"Hello {name}"

    @register
    def be_awesome(name):
        return f"Yo {name}, together we are the awesomest!"

    def randomly_greet(name):
        greeter, greeter_func = random.choice(list(PLUGINS.items()))
        print(f"Using {greeter!r}")
        return greeter_func(name)
```

## decoradores en clase
funcionan exactamente igual , la unica diferencia es que como argumento se pasa una clase en lugar de una funcion,  puedes aplicar un decorador a cada metodo como si de una funcion se tratase o a la clase completa .

## decoradores anidados

podemos agregar varios decoradores apilados

```python

    from decorators import debug, do_twice

    @debug
    @do_twice
    def greet(name):
        print(f"Hello {name}")

```

Estos decoradores son ejecutados en el orden que son llamados. debug(do_twice(greet())).

## Se pueden declarar decoradores con argumentos

```python
    @repeat(num_times=4)
    def greet(name):
        print(f"Hello {name}")


    def repeat(num_times):
        def decorator_repeat(func):
            ...  # Create and return a wrapper function
        return decorator_repeat
```

## decoradores para trackear estado

decorador que indica cuantas veces fue llamada la funcion, El numero de veces que se llamo a la funcion queda almacenado en el atributo ```num_calls```

```python
    import functools

    def count_calls(func):
        @functools.wraps(func)
        def wrapper_count_calls(*args, **kwargs):
            wrapper_count_calls.num_calls += 1
            print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
            return func(*args, **kwargs)
        wrapper_count_calls.num_calls = 0
        return wrapper_count_calls

    @count_calls
    def say_whee():
        print("Whee!")
    
    say_whee.num_calls
```

## clases como decoradores

podemos ocupar una clase como un decorador si sobree escribimos el metodo ```__call__```

```python
    import functools

    class CountCalls:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func
            self.num_calls = 0

        def __call__(self, *args, **kwargs):
            self.num_calls += 1
            print(f"Call {self.num_calls} of {self.func.__name__!r}")
            return self.func(*args, **kwargs)

    @CountCalls
    def say_whee():
        print("Whee!")
```

## ejemplos de la vida real parte dos

## crear un singleton

```python
    import functools

    def singleton(cls):
        """Make a class a Singleton class (only one instance)"""
        @functools.wraps(cls)
        def wrapper_singleton(*args, **kwargs):
            if not wrapper_singleton.instance:
                wrapper_singleton.instance = cls(*args, **kwargs)
            return wrapper_singleton.instance
        wrapper_singleton.instance = None
        return wrapper_singleton

    @singleton
    class TheOne:
        pass
```
## caching return values

```python
    import functools
    from decorators import count_calls

    def cache(func):
        """Keep a cache of previous function calls"""
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache.cache:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            return wrapper_cache.cache[cache_key]
        wrapper_cache.cache = dict()
        return wrapper_cache

    @cache
    @count_calls
    def fibonacci(num):
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)
```

## agregar informacion sobre unidades

```python
    def set_unit(unit):
        """Register a unit on a function"""
        def decorator_set_unit(func):
            func.unit = unit
            return func
        return decorator_set_unit
    
    import math

    @set_unit("cm^3")
    def volume(radius, height):
        return math.pi * radius**2 * height


    >>> volume(3, 5)
    141.3716694115407

    >>> volume.unit
    'cm^3'
```


