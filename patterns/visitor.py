""" Поведенческий шаблон проектирования 'Посетитель' """

from abc import ABC, abstractmethod


class Spy(ABC):
    """ Шпион - посетитель """
    @abstractmethod
    def visit_military_base(self, military_base: 'MilitaryBase'):
        """ Посетить военную базу морского флота """
        raise NotImplementedError()

    @abstractmethod
    def visit_headquarters(self, headquarters: 'Headquarters'):
        """ Посетить центральный штаб армии """
        raise NotImplementedError()


class MilitaryFacility(ABC):
    """ Военный объект - посещаемый объект """

    @abstractmethod
    def accept(self, spy: Spy):
        """ Принять шпиона-посетителя """
        raise NotImplementedError()


class MilitaryBase(MilitaryFacility):
    """ Военная база подводного флота """
    def __init__(self):
        self._secret_draftings = 1
        self._nuclear_submarines = 1

    def __repr__(self):
        return (f"На военной базе находится {self._nuclear_submarines} атомных подводных лодок "
                f"и {self._secret_draftings} секретных чертежей")

    def accept(self, spy: Spy):
        spy.visit_military_base(self)

    def remove_secret_draftings(self):
        if self._secret_draftings:
            self._secret_draftings -= 1

    def remove_nuclear_submarines(self):
        if self._nuclear_submarines:
            self._nuclear_submarines -= 1

    @property
    def is_combat_ready(self) -> bool:
        return self._nuclear_submarines > 0


class Headquarters(MilitaryFacility):
    """ Центральный штаб армии """
    def __init__(self):
        self._generals = 3
        self._secret_documents = 2

    def __repr__(self):
        return f"В штабе находится {self._generals} генералов и {self._secret_documents} секретных документов"

    def accept(self, spy: Spy):
        spy.visit_headquarters(self)

    def remove_general(self):
        if self._generals:
            self._generals -= 1

    def remove_secret_documents(self):
        if self._secret_documents:
            self._secret_documents -= 1

    @property
    def is_command_ready(self):
        return self._generals > 0


class ScoutSpy(Spy):
    """ Разведчик (конкретный шпион) """
    def __init__(self):
        self._collected_info = {}

    def visit_military_base(self, military_base: MilitaryBase):
        self._collected_info['base'] = (f"'Военная база:\n\t{military_base}\n"
                                        f"\tБоеготовность: {'Да' if military_base.is_combat_ready else 'нет'}'")

    def visit_headquarters(self, headquarters: Headquarters):
        self._collected_info['headquarters'] = \
            (f"Центральный штаб:\n\t{headquarters}\n"
             f"\tКомандование: {'Функционирует' if headquarters.is_command_ready else 'Не функционирует'}")

    def report(self) -> str:
        return f"Информация от разведчика:\n{'\n'.join(self._collected_info.values())}\n"


class JamesBond(Spy):
    """ Джеймс Бонд (другой конкретный шпион) """

    def visit_military_base(self, military_base: MilitaryBase):
        military_base.remove_secret_draftings()     # похищает секретные чертежи
        military_base.remove_nuclear_submarines()   # и взрывает атомную подводную лодку

    def visit_headquarters(self, headquarters: Headquarters):
        headquarters.remove_general()
        headquarters.remove_general()
        headquarters.remove_secret_documents()
        headquarters.remove_general()               # Уничтожает всех генералов
        headquarters.remove_secret_documents()      # и похищает все секретные документы


if __name__ == "__main__":
    base = MilitaryBase()
    hq = Headquarters()

    facilities: tuple[MilitaryFacility, ...] = (base, hq)

    scout = ScoutSpy()
    print("Отправляется разведчик")
    for f in facilities:
        f.accept(scout)
    print(scout.report())

    spy = JamesBond()
    print('Отправляется Бонд на задание')
    for f in facilities:
        f.accept(spy)

    print("Снова отправляется разведчик обновить данные")
    for f in facilities:
        f.accept(scout)
    print(scout.report())
