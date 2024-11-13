""" Поведенческий шаблон проектирования 'Состояние' """

from abc import ABC, abstractmethod


class AbstractState(ABC):
    @abstractmethod
    def eat(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def find_food(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def move(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def dream(self) -> str:
        raise NotImplementedError()


class SleepState(AbstractState):
    def eat(self) -> str:
        return 'не может есть, пока спит'

    def find_food(self) -> str:
        return 'ищет еду, но только в своих мечтах'

    def move(self) -> str:
        return 'не может двигаться, пока спит'

    def dream(self) -> str:
        return 'спит и видит чудный сон'


class OnGroundState(AbstractState):
    def eat(self) -> str:
        return 'вываливает на пузо добытых моллюсков и начинает неспешно их есть'

    def find_food(self) -> str:
        return 'находит дурно пахнущую, но вполне съедобную тушу выбросившегося на берег кита'

    def move(self) -> str:
        return 'неуклюже ползет вдоль береговой линии'

    def dream(self) -> str:
        return 'на мгновение останавливается, замечтавшись об одной знакомой самке'


class InWaterState(AbstractState):
    def eat(self) -> str:
        return 'не может есть в воде'

    def find_food(self) -> str:
        return 'вспахивает бивнями морское дно, вылавливая моллюсков своими вибриссами'

    def move(self) -> str:
        return 'грациозно рассекает волны мирового океана'

    def dream(self) -> str:
        return 'не спит и не мечтает в воде - это слишком сложно'


class Walrus(AbstractState):
    def __init__(self, state: AbstractState):
        self._state = state

    def change_sate(self, state: AbstractState):
        self._state = state

    def eat(self) -> str:
        return self._state.eat()

    def find_food(self) -> str:
        return self._state.find_food()

    def move(self) -> str:
        return self._state.move()

    def dream(self) -> str:
        return self._state.dream()

    def execute(self, operation):
        match operation:
            case 'eat':
                print(self.eat())
            case 'find_food':
                print(self.find_food())
            case 'move':
                print(self.move())
            case 'dream':
                print(self.dream())
            case _:
                print("Морж не умеет такого делать")


if __name__ == "__main__":
    operations = ('eat', 'find_food', 'move', 'dream')
    sleep = SleepState()
    on_ground = OnGroundState()
    in_water = InWaterState()
    walrus = Walrus(on_ground)

    print("На берегу")
    for operation in operations:
        walrus.execute(operation)
    print("")

    print("В воде")
    walrus.change_sate(in_water)
    for operation in operations:
        walrus.execute(operation)
    print("")

    print("Во сне")
    walrus.change_sate(sleep)
    for operation in operations:
        walrus.execute(operation)