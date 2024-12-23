""" Структурный шаблон проектирования 'Фасад' """


class Facade:
    """
    Класс Фасада предоставляет простой интерфейс для сложной логики одной или
    нескольких подсистем. Фасад делегирует запросы клиентов соответствующим
    объектам внутри подсистемы. Фасад также отвечает за управление их жизненным
    циклом. Все это защищает клиента от нежелательной сложности подсистемы.
    """
    def __init__(self, subsystem_1: 'Subsystem1', subsystem_2: 'Subsystem2'):
        """
        В зависимости от потребностей вашего приложения вы можете предоставить
        Фасаду существующие объекты подсистемы или заставить Фасад создать их
        самостоятельно.
        """
        self._subsystem_1 = subsystem_1
        self._subsystem_2 = subsystem_2

    def operation(self):
        """
        Методы Фасада удобны для быстрого доступа к сложной функциональности
        подсистем. Однако клиенты получают только часть возможностей подсистемы.
        """
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_1.operation_1())
        results.append(self._subsystem_2.operation_1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_1.operation_n())
        results.append(self._subsystem_2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    Подсистема может принимать запросы либо от фасада, либо от клиента напрямую.
    В любом случае, для Подсистемы Фасад – это ещё один клиент, и он не является
    частью Подсистемы.
    """
    def operation_1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Некоторые фасады могут работать с разными подсистемами одновременно.
    """

    def operation_1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self):
        return "Subsystem2: Fire!"


def client_code(facade: Facade):
    """
    Клиентский код работает со сложными подсистемами через простой интерфейс,
    предоставляемый Фасадом. Когда фасад управляет жизненным циклом подсистемы,
    клиент может даже не знать о существовании подсистемы. Такой подход
    позволяет держать сложность под контролем.
    """
    print(facade.operation(), end="")


if __name__ == "__main__":
    # В клиентском коде могут быть уже созданы некоторые объекты подсистемы. В
    # этом случае может оказаться целесообразным инициализировать Фасад с этими
    # объектами вместо того, чтобы позволить Фасаду создавать новые экземпляры.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)