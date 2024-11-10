""" Порождающий шаблон проектирования 'Фабричный метод' """
from abc import ABC, abstractmethod
from enum import StrEnum

class Localizes(StrEnum):
    FRENCH = "French"
    SPANISH = "Spanish"
    ENGLISH = "English"

def factory(language : Localizes = Localizes.ENGLISH) -> 'AbstractLocalizer':
    """ The Factory Method """
    localizes = {
            Localizes.FRENCH: FrenchLocalizer,
            Localizes.SPANISH: SpanishLocalizer,
            Localizes.ENGLISH: EnglishLocalizer
        }
    return localizes[language]()


class AbstractLocalizer(ABC):
    """ Абстрактный продукт """

    @abstractmethod
    def localize(self, msg):
        raise NotImplemented


class FrenchLocalizer(AbstractLocalizer):
    """ Возвращает французскую версию продукта """
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(AbstractLocalizer):
    """ Возвращает испанскую версию продукта """
    def __init__(self):

        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer(AbstractLocalizer):
    """ Возвращает английскую версию продукта """
    def localize(self, msg):
        return msg

if __name__ == "__main__":
    f = factory(Localizes.FRENCH)
    s = factory(Localizes.SPANISH)
    e = factory(Localizes.ENGLISH)

    for msg in ("car", "bike", "cycle"):
        print(f.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))