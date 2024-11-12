""" Поведенческий шаблон проектирования 'Интерпретатор' """
# Система для вычисления и манипулирования булевыми выражениями.

from abc import abstractmethod, ABC


class Context:
    """ Контекст среды исполнения интерпретатора """
    def __init__(self, variables: dict = None):
        self._variables = variables if variables is not None else {}

    def lookup(self, name: str) -> bool:
        """
        Получает значение переменной по ее имени
        :param name: имя переменной
        :return:
        """
        if name in self._variables:
            return self._variables[name]
        raise ContextException(f"Неизвестная переменная '{name}'")

    def assign(self, name: str, value: bool):
        """
        Назначает значение переменной по ее имени
        :param name: имя переменной
        :param value: значение переменной
        """
        self._variables[name] = value


class AbstractBooleanExp(ABC):
    """ Абстрактное логическое выражение """

    @abstractmethod
    def evaluate(self, context: Context) -> bool:
        """ Получение результата логического выражения """
        raise NotImplemented()


class ConstantExp(AbstractBooleanExp):
    """ Логическая константа """
    def __init__(self, value: bool):
        """
        Конструктор
        :param value: значение выражения (True или False)
        """
        self._value = value

    def evaluate(self, context: Context) -> bool:
        return self._value


class VariableExp(AbstractBooleanExp):
    """ Логическая переменная (значение переменных хранится в объекте контекста интерпретатора) """
    def __init__(self, name: str):
        """
        Конструктор
        :param name: название переменной
        """
        self._name = name

    def evaluate(self, context: Context) -> bool:
        return context.lookup(self._name)


class AbstractBinaryOperationExp(AbstractBooleanExp, ABC):
    """ Абстрактный класс для бинарных логических операций """
    def __init__(self, left: AbstractBooleanExp, right: AbstractBooleanExp):
        """
        Конструктор
        :param left: левый операнд
        :param right: правый операнд
        """
        self._left = left
        self._right = right


class AndExp(AbstractBinaryOperationExp):
    """ Конъюнкция """

    def evaluate(self, context: Context) -> bool:
        return self._left.evaluate(context) and self._right.evaluate(context)


class OrExp(AbstractBinaryOperationExp):
    """ Дизъюнкция """

    def evaluate(self, context: Context) -> bool:
        return self._left.evaluate(context) or self._right.evaluate(context)


class NotExp(AbstractBooleanExp):
    """ Отрицание """
    def __init__(self, operand: AbstractBooleanExp):
        """
        Constructor
        :param operand: операнд, к которому применяется операция
        """
        self._operand = operand

    def evaluate(self, context: Context) -> bool:
        return not self._operand.evaluate(context)


class ContextException(Exception):
    """ Исключение, прокидываемое в случае некорректной работы с данным классом """
    pass


def execute_test(context: Context, x: bool, y: bool):
    """ Функция для выполнения тестирования интерпретатора """
    context.assign('x', x)
    context.assign('y', y)
    expression = OrExp(     # (True and x) or (у and (not x))
        AndExp(ConstantExp(True), VariableExp('x')),
        AndExp(VariableExp('y'), NotExp(VariableExp('x')))
    )
    print(expression.evaluate(context))


if __name__ == "__main__":
    print("OUTPUT")
    context = Context()
    execute_test(context, True, False)
    execute_test(context, False, True)
    execute_test(context, False, False)