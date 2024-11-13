""" Поведенческий шаблон проектирования 'Стратегия' """
from abc import ABC, abstractmethod


class People:
    tool = None

    def __init__(self, name):
        self._name = name

    def set_tool(self, tool: 'ToolBase'):
        self.tool = tool

    def write(self, text):
        self.tool.write(self._name, text)


class ToolBase(ABC):
    """ Семейство алгоритмов `Инструмент написания` """
    @abstractmethod
    def write(self, name, text):
        raise NotImplementedError()


class PenTool(ToolBase):
    """ Ручка """

    def write(self, name, text):
        print(f"{name} ручкой {text}")


class BrushTool(ToolBase):
    """ Кисть """

    def write(self, name, text):
        print(f"{name} кистью {text}")


class Student(People):
    """ Студент """
    tool = PenTool()


class Painter(People):
    """ Художник """
    tool = BrushTool()


if __name__ == "__main__":
    maxim = Student("Максим")
    maxim.write("Пишу стихи про лето")

    sasha = Painter("Саша")
    sasha.write("Рисую иллюстрацию про лето")

    sasha.set_tool(PenTool())
    sasha.write("А теперь пишу про свою иллюстрацию")
