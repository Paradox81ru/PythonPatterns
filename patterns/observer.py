""" Поведенческий шаблон проектирования 'Наблюдатель' """
from abc import ABC, abstractmethod


class Observer(ABC):
    """ Абстрактный наблюдатель """

    @abstractmethod
    def update(self, message: str):
        """ Получает новое сообщение """
        raise NotImplementedError()


class Observable(ABC):
    """ Абстрактный наблюдаемый """
    def __init__(self):
        self._observers: list[Observer] = []
        """ Список наблюдателей """

    def register(self, observer: Observer):
        """ Регистрирует нового наблюдателя на подписку """
        self._observers.append(observer)

    def notify_observers(self, message: str):
        """ Передаёт сообщения всем наблюдателям, подписанным на события """
        for observer in self._observers:
            observer.update(message)


class Newspaper(Observable):
    """ Газета, за новостями в которой следят тысячи людей """
    def add_news(self, news):
        """ Выпуск очередной новости """
        self.notify_observers(news)


class Citizen(Observer):
    """ Обычный гражданин, который любит почитать с утра газету """
    def __init__(self, name: str):
        """
        Конструктор
        :param name: имя гражданина
        """
        self.name = name

    def update(self, message: str):
        print(f"{self.name} узнал следующее: {message}")


if __name__ == "__main__":
    newspaper = Newspaper()
    newspaper.register(Citizen('Иван'))
    newspaper.register(Citizen('Василий'))
    newspaper.add_news("Какая-то интересная новость")