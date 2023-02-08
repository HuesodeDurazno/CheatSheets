# Property en python 

En python no hay modificadores de acceso , todo es publico o No publico.

Properties nos permite crear un metodo que se comporte como un atributo 

## Metodo property

```python
    property(fget=None, fset=None, fdel=None, doc=None)
```

| Argument | Description |
| -------- | ----------- |
|fget	|   Function that returns the value of the managed attribute |
|fset	|   Function that allows you to set the value of the managed attribute |
|fdel	|   Function to define how the managed attribute handles deletion |
|doc	|   String representing the property’s docstring |

## Uso

```python

    # circle.py

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        def _get_radius(self):
            print("Get radius")
            return self._radius

        def _set_radius(self, value):
            print("Set radius")
            self._radius = value

        def _del_radius(self):
            print("Delete radius")
            del self._radius

        radius = property(
            fget=_get_radius,
            fset=_set_radius,
            fdel=_del_radius,
            doc="The radius property."
        )
```

## Uso con decorator

```python
    # circle.py

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            """The radius property."""
            print("Get radius")
            return self._radius

        @radius.setter
        def radius(self, value):
            print("Set radius")
            self._radius = value

        @radius.deleter
        def radius(self):
            print("Delete radius")
            del self._radius
```
