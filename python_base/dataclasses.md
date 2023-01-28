# Dataclasses

## Que son?

Es una clase designada para almacenar valores. No cuentan con otros metodos, Usadas para almacenar informacion que sera pasada entre diferentes partes del programa o sistema.

## Ejemplo 

Normalmente tenemos una clase como esta

```python

    class Person():
    
    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

```

Con dataclasses solo definimos el tipo de dato y podemos asignar valores default.

Recordemos que en python siempre los atributos con valores por default van despues de los atributos sin estos.

Dataclasses funciona con Typing

```python
    from typing import Tuple

    @dataclass
    class Person():
        name: str
        age: int
        height: float
        email: str
        house_coordinates: Tuple

```

Para acceder a los atributos se hace de manera normal 

```Python
    print(person.name)
    >>> Joe

```



## Representacion y comparacion

En una clase normal sobre escribiriamos ```__repr__``` para cambiar la representacion de un objeto

En data classes no es necesario.

```python

    @dataclass
    class Person():
        name: str
        age: int
        height: float
        email: str

    person = Person('Joe', 25, 1.85, 'joe@dataquest.io')
    print(person)

    >>>Person(name='Joe', age=25, height=1.85, email='joe@dataquest.io')
    # tambien podemos sobre escribir __repr__ si no nos gusta esta representacion
```

Con dataclasses podemos comparar dos instancias sin mayor problema

```python
    @dataclass
    class Person():
        name: str = 'Joe'
        age: int = 30
        height: float = 1.85
        email: str = 'joe@dataquest.io'

    print(Person() == Person())

    >>> True
    # dataclasses tambien sobre escribe el metodo __eq__ por nosotros :D
```

## The @dataclass parameters

como mencionamos ```__init__```,```__repr__```,```__eq__``` son sobre escritos por nosotros ,podemos indicarle al decorador si queremos que estos metodos sean sobre escritos o no, con los parametros ```init```,```repr```,```eq``` estos estan seteados como ***True*** por default.

Existen otros parametros como lo son ```order``` y ```frozen```, el primero abilita el sorting y el segundo hace que no se puedan cambiar los valores de la clase despues de ser creados.

(hay mas pero ahi dejo la documentacion xd ,  https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass)

### sorting

```python

    @dataclass(order=True)
    class Person():
        name: str
        age: int
        height: float
        email: str

    joe = Person('Joe', 25, 1.85, 'joe@dataquest.io')
    mary = Person('Mary', 43, 1.67, 'mary@dataquest.io')

    print(joe > mary)

    >>>False

```
Para hacer la comparacion verifica que "J" esta antes que "M" , si los nombres fueran iguales seguiria con el siguiente atributo , para controlar las comparaciones ocupamos dos herramientas mas , la primera ```field```

Es una funcion para customizar un atributo de una clase individualmente, nos permite definir nuevos atributos que dependen de otro, y solo se crearan despues del que objeto sea inizializado.

```init=False``` quiere decir que no estara en ```__init``` y por lo tanto no sera mostrado en ```__repr__```, el otro parametro sobre escribe el ```__repr__```

El otro metodo para sorbre escribir el index es ```__post_init__``` este metodo se ejecuta justo despues de ```__init__``` , asignamos age para indicar que queremos comparar por medio de ese campo.


```python
    @dataclass(order=True)
    class Person():
        sort_index: int = field(init=False, repr=False)
        name: str
        age: int
        height: float
        email: str

        def __post_init__(self):
            self.sort_index = self.age
```

## Clases inmutables

si indicamos **frozen=True** la clase sera constante y si queremos modificarla tendremos un error,

Si nuestra clase tiene un objeto mutable el atributo puede cambiar incluso si la clase es frozen.

```python
    @dataclass(frozen=True)
    class People():
        people: List[Person]

    @dataclass(frozen=True)
    class Person():
        name: str
        age: int
        height: float
        email: str


    joe = Person('Joe', 25, 1.85, 'joe@dataquest.io')
    mary = Person('Mary', 43, 1.67, 'mary@dataquest.io')

    two_people = People([joe, mary])
    print(two_people)


    >> People(people=[Person(name='Joe', age=25, height=1.85, email='joe@dataquest.io'), Person(name='Mary', age=43, height=1.67, email='mary@dataquest.io')])

    two_people.people[0] = Person('Joe', 35, 1.85, 'joe@dataquest.io')
    print(two_people.people[0])

    >> Person(name='Joe', age=35, height=1.85, email='joe@dataquest.io')
```

## herencia 

Tambien soporta herencia , pero si la clase padre tiene valores por default, entonces la clase hija tambien debe de tener todos los valores con un valor por default  o marca error 


```python
    @dataclass(order=True)
    class Person():
        name: str
        age: int
        height: float
        email: str

    @dataclass(order=True)
    class Employee(Person):
        salary: int
        departament: str
```






