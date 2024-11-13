""" Поведенческий шаблон проектирования 'Хранитель' """


class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state


class Caretaker:
    def __init__(self, memento: Memento):
        self._memento = memento

    def get_memento(self) -> Memento:
        return self._memento


class Originator:
    def __init__(self, state: str):
        self._state = state

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    def save_state(self) -> Memento:
        return Memento(self._state)

    def restore_state(self, memento: Memento):
        self._state = memento.get_state()


if __name__ == '__main__':
    originator = Originator(state='on')
    print(originator.state)

    caretaker = Caretaker(originator.save_state())

    originator.state = 'off'
    print(originator.state)

    originator.restore_state(caretaker.get_memento())
    print(originator.state)
