""" Поведенческий шаблон проектирования 'Команда' """
from abc import ABC, abstractmethod


class Receiver:
    """ Объект, который получит и выполнит команду """

    @classmethod
    def run_command_1(cls):
        """ A set of instructions to run """
        print("Executing Command 1")

    @classmethod
    def run_command_2(cls):
        """ A set of instructions to run """
        print("Executing Command 2")


class AbstractCommand(ABC):
    """ Командный интерфейс, который будут реализовывать все команды. """
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        """ Необходимый метод execute, который будут использовать все объекты command """
        raise NotImplementedError()


class Invoker:
    """ Объект, который отправляет команду получателю. Например, кнопка. """
    def __init__(self):
        self._commands: dict[str, AbstractCommand] = {}

    def register(self, command_name: str, command: AbstractCommand):
        """ Регистрируйте команды в вызывающем устройстве """
        self._commands[command_name] = command

    def execute(self, command_name):
        """ Выполнять указанную зарегистрированную команду """
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Command1(AbstractCommand):
    def execute(self):
        self._receiver.run_command_1()


class Command2(AbstractCommand):
    def execute(self):
        self._receiver.run_command_2()


if __name__ == "__main__":
    _receiver = Receiver()

    command1 = Command1(_receiver)
    command2 = Command2(_receiver)

    invoker = Invoker()
    invoker.register("1", command1)
    invoker.register("2", command2)

    invoker.execute("1")
    invoker.execute("2")
    invoker.execute("1")
    invoker.execute("2")