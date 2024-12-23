""" Порождающий шаблон проектирования 'Прототип' """

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """ Регистрирует объект """
        self._objects[name] = obj

    def unregister_object(self, name):
        """ Отменяет регистрацию объекта """
        del self._objects[name]

    def clone(self, name,  **attr):
        """ Клонирует зарегистрированный объект """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class A:
    def __init__(self, x, y, z, garbage):
        self.x = x
        self.y = y
        self.z = z
        self.garbage = garbage

    def __str__(self):
        return f"{id(self)}, {self.x}, {self.y}, {self.z}, {self.garbage}"


if __name__ == "__main__":
    a = A(3, 8, 15, [38, 11, 19])
    prototype = Prototype()
    prototype.register_object('object', a)
    b = prototype.clone('object')
    print(f"a is b = {a is b}")
    c = prototype.clone('object', x=1, y=2, garbage=[88, 1])
    print([str(i) for i in (a, b, c)])
