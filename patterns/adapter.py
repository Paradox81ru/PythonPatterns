""" Шаблон проектирования 'Адаптер' """
from abc import ABC, abstractmethod

class AbstractOldPrinter(ABC):
    @abstractmethod
    def print_document(self, document):
        raise NotImplemented


class NewPrinter:
    def print(self, text):
        print(f"Printing new document: {text}")


class OldPrinter(AbstractOldPrinter):
    def print_document(self, document):
        print(f"Printing old document: {document}")


class PrintAdapter(AbstractOldPrinter):
    def __init__(self, new_printer: NewPrinter):
        self.new_printer = new_printer

    def print_document(self, document):
        self.new_printer.print(document)


class Client:
    def print_client(self, print_class: AbstractOldPrinter):
        print_class.print_document("Document name")


if __name__ == "__main__":
    client = Client()
    old_print = OldPrinter()
    client.print_client(old_print)

    new_printer = NewPrinter()
    print_adapter = PrintAdapter(new_printer)
    client.print_client(print_adapter)
