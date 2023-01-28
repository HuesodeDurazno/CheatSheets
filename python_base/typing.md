# Typing

## Sintaxis basica

```python
    def headline(text: str, align: bool = True) -> str:
        ...
```
## Recomendasiones PEP8

Use normal rules for colons, that is, no space before and one space after a colon: text: str.

Use spaces around the = sign when combining an argument annotation with a default value: align: bool = True.

Use spaces around the -> arrow: def headline(...) -> str.

## Libreria para hacer check de types

Una herramienta util para comprobar que typings se estan siguiendo durante la ejecucion del programa es con ***mypy**

puedes instalar la libreria desde pip

```bash
    pip install mypy 
```

Para chequear el tipado

```
    mypy file.py
```

## ventajas de ocupar typing

1. Mejora la documentacion
2. Mejora el funcionamiento de los editores de codigo
3. Ayuda a contruir y mantener una arquitectura limpia

## observar anotaciones

Puedes observar las anotaciones con el metodo ```__anotations__```

```python
    import math

    def circumference(radius: float) -> float:
        return 2 * math.pi * radius

    >>> circumference(1.23)
    7.728317927830891

    >>> circumference.__annotations__
    {'radius': <class 'float'>, 'return': <class 'float'>}
```

## Anotaciones en variables

```python
    integer:int
    pi: float = 3.142
    nothing: tuple
    list_large:list
    set_large:set
```

## Typing en colecciones

```python
    from typing import Dict, List, Tuple

    names: List[str] = ["Guido", "Jukka", "Ivan"]
    version: Tuple[int, int, int] = (3, 7, 1)
    options: Dict[str, bool] = {"centered": False, "capitalize": True}
    comples: List[Tuple[str, str]]
```
Otra forma de agregar typing a estructuras complejas es 

```python
    from typing import List, Tuple

    Card = Tuple[str, str]
    Deck = List[Card]
```

## fucniones sin retorno

Para indicar que no tienen retorno , en vez de escribir -> None , puedes escribir 

```python
    from typing import NoReturn

    def black_hole() -> NoReturn:
        raise Exception("There is no going back ...")
```

## indicar que una funcion puede resivir cualquier tipo de iterable

Sequence indica cualquier objeto que tenga un metodo ```__len__``` y ```__getitem__```

```python
    from typing import List, Sequence

    def square(elems: Sequence[float]) -> List[float]:
        return [x**2 for x in elems]
```

## indicar que se puede recibir cualquier cosa

Podemos ocupar Any

```python
    import random
    from typing import Any, Sequence

    def choose(items: Sequence[Any]) -> Any:
        return random.choice(items)
```

## Clases como anotacion
Podemos ocupar clases como anotaciones
```python
    class Deck:
        pass

    class Player:
        def __init__(self, name: str, hand: Deck) -> None:
            self.name = name
            self.hand = hand
    

    # si la clase aun no esta definida, podemos ocupar 

    class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        ...

```

## Callables

Quiere decir que el tipo en el parametro o el retorno es algo que puede ser ejecutable

```python
    from typing import Callable

    def do_twice(func: Callable[[str], str], argument: str) -> None:
        print(func(argument))
        print(func(argument))

```

