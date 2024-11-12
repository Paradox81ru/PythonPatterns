""" Структурный шаблон проектирования 'Компоновщик' """
from abc import ABC, abstractmethod


class Component(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    сложных объектов структуры.
    """

    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> 'Component':
        return self._parent

    @parent.setter
    def parent(self, val: 'Component'):
        self._parent = val

    def is_composite(self) -> bool:
        """ Может ли компонент иметь вложенные объекты. """
        return False

    @abstractmethod
    def operation(self) -> str:
        raise NotImplemented()


class Leaf(Component):
    """
    Класс Лист представляет собой конечные объекты структуры. Лист не может
    иметь вложенных компонентов.

    Обычно объекты Листьев выполняют фактическую работу, тогда как объекты
    Контейнера лишь делегируют работу своим подкомпонентам.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты. Обычно объекты Контейнеры делегируют фактическую работу своим
    детям, а затем «суммируют» результат.
    """
    def __init__(self):
        super().__init__()
        self._children: list[Component] = []

    def operation(self) -> str:
        """
        Контейнер выполняет свою основную логику особым образом. Он проходит
        рекурсивно через всех своих детей, собирая и суммируя их результаты.
        Поскольку потомки контейнера передают эти вызовы своим потомкам и так
        далее, в результате обходится всё дерево объектов.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

    def add(self, component: 'Component') -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: 'Component') -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True


def client_code_1(component: Component):
    """ Клиентский код работает со всеми компонентами через базовый интерфейс. """
    print(f"RESULT: {component.operation()}", end="")


def client_code_2(component1: Composite, component2: Component):
    """
    Благодаря тому, что операции управления потомками объявлены в базовом классе
    Компонента, клиентский код может работать как с простыми, так и со сложными
    компонентами, вне зависимости от их конкретных классов.
    """
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать простые компоненты-
    # листья...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code_1(simple)
    print("\n")

    # ...а также сложные контейнеры.
    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code_1(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code_2(tree, simple)
