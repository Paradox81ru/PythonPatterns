""" Структурный шаблон проектирования 'Заместитель' """
from abc import ABC, abstractmethod


class AbstractMath(ABC):
    @abstractmethod
    def add(self, x, y):
        raise NotImplementedError()

    @abstractmethod
    def sub(self, x, y):
        raise NotImplementedError()

    @abstractmethod
    def mul(self, x, y):
        raise NotImplementedError()

    @abstractmethod
    def div(self, x, y):
        raise NotImplementedError()


class Math(AbstractMath):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x /y


class ProxyMath(AbstractMath):
    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        return float('inf') if y == 0 else self.math.div(x, y)


if __name__ == "__main__":
    p = ProxyMath()
    x, y = 4, 2
    print(f"4 + 2 = {p.add(x, y)}")
    print(f"4 - 2 = {p.sub(x, y)}")
    print(f"4 * 2 = {p.mul(x, y)}")
    print(f"4 / 2 = {p.div(x, y)}")
    y = 0
    print(f"4 / 2 = {p.div(x, y)}")