class Model:
    _fields = []

    # Deserialize request JSON in constructor
    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            if name in self._fields:
                setattr(self, name, value)

    # Serialize object into JSON
    def serialize(self):
        return self.__dict__

    def __str__(self):
        return f'{self.__dict__!s}'

    def __repr__(self):
        return f"{self.__class__!r}({','.join(self.__dict__.values())!r})"


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.ty}, got {type(value)}')
        super().__set__(instance, value)


class Integer(Typed):
    ty = int


class Float(Typed):
    ty = float


class String(Typed):
    ty = str
