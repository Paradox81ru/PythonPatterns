""" Поведенческий шаблон проектирования 'Шаблонный метод """
from abc import ABC, abstractmethod


class Unit(ABC):
    """ Абстрактный отряд """
    def __init__(self, speed: int):
        self._speed = speed

    def hit_and_run(self):
        """ Шаблонный метод """
        self._move('вперёд')
        self._stop()
        self._attack()
        self._move("назад")

    @abstractmethod
    def _attack(self):
        raise NotImplementedError()

    @abstractmethod
    def _stop(self):
        raise NotImplementedError()

    def _move(self, direction: str):
        """
        Передвижение - у всех отрядов одинаковое, в шаблон не входит
        :param direction: направление движения
        """
        self._output(f'движется {direction}, со скоростью {self._speed}')

    def _output(self, message: str):
        """
        Вспомогательный метод вывода сообщений, в шаблон не входит
        :param message: выводимое сообщение
        :return:
        """
        print(f"Отряд типа {self.__class__.__name__} {message}")


class Archers(Unit):
    """ Лучники """
    def _attack(self):
        self._output("обстреливает врага")

    def _stop(self):
        self._output("останавливается в 100 шагах от врага")


class Cavalryman(Unit):
    def _attack(self):
        self._output('на полном скаку врезается во вражеский строй')

    def _stop(self):
        self._output('летит вперед, не останавливаясь')


if __name__ == "__main__":
    print("OUTPUT")
    archers = Archers(4)
    archers.hit_and_run()
    cavalryman = Cavalryman(8)
    cavalryman.hit_and_run()