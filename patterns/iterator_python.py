"""
Поведенческий шаблон проектирования 'Итератор' на Python

Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
"""

from collections.abc import Iterable, Iterator


class AlphabeticalOrderIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """
    _position: int = None
    """ текущая позиция """

    _reverse: bool = False
    """ направление обхода """

    def __init__(self, collection: 'WordsCollection', reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        Возвращает следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        :return:
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            return value
        except IndexError:
            raise StopIteration()


class WordsCollection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """
    def __init__(self, collection: list = None):
        self._collection = collection if collection is not None else []

    def __getitem__(self, index: int):
        return self._collection[index]

    def __delitem__(self, index: int):
        if index < len(self._collection):
            del self._collection[index]

    def __iter__(self):
        """
        Возвращает объект итератора, по умолчанию возвращается итератор с сортировкой по возрастанию.
        :return:
        """
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, value):
        self._collection.append(value)


if __name__ == "__main__":
    collection = WordsCollection(['First', "Second"])
    collection.add_item("Third")
    collection.add_item("Four")
    collection.add_item("Five")

    del collection[3]

    print("Straight traversal:")
    print(", ".join(collection))
    print("")

    print("Reverse traversal:")
    print(", ".join(collection.get_reverse_iterator()))