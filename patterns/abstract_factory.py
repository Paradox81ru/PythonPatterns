""" Порождающий шаблон проектирования 'Абстрактная фабрика' """
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """ The Abstract Factory """

    @abstractmethod
    def create_browser(self) -> 'AbstractBrowser':
        raise NotImplemented

    @abstractmethod
    def create_messenger(self) -> 'AbstractMessenger':
        raise NotImplemented


class VanillaProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()


class SecureProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()


class AbstractBrowser(ABC):
    """ Creates "Abstract Product A" """

    # Interface - Create Search Toolbar
    @abstractmethod
    def create_search_toolbar(self):
        raise NotImplemented

    # Interface - Create Browser Window
    @abstractmethod
    def create_browser_window(self):
        raise NotImplemented


class AbstractMessenger(ABC):
    """ Creates "Abstract Product B" """

    # Interface - Create Messenger Window
    @abstractmethod
    def create_messenger_window(self):
        raise NotImplemented


class VanillaBrowser(AbstractBrowser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window
    def create_browser_window(self):
        print("Browser Window Created")


class VanillaMessenger(AbstractMessenger):
    """
        Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Messenger Window Created")


class SecureBrowser(AbstractBrowser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Interface - Create Browser Window
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")

class SecureMessenger(AbstractMessenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")


if __name__ == '__main__':
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        browser = factory.create_browser()
        messenger = factory.create_messenger()
        browser.create_browser_window()
        browser.create_search_toolbar()
        messenger.create_messenger_window()