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

