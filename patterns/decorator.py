""" Шаблон проектирования 'Декоратор' """
from abc import ABC, abstractmethod


class AbstractBlock(ABC):
    """ Абстрактный блок """
    @abstractmethod
    def draw(self):
        raise NotImplemented()


class TerminatorBlock(AbstractBlock):
    """ Терминальный блок (начало/конец, вход/выход) """
    def draw(self):
        print("Terminator block drawing ... ")


class ProcessBlock(AbstractBlock):
    """ Блок - процесс (один или несколько операторов)   """
    def draw(self):
        print("Process block drawing ... ")


class AbstractBlockDecorator(AbstractBlock):
    """ Абстрактный декоратор блоков """
    def __init__(self, decorate: AbstractBlock):
        # _decorate - ссылка на декорируемый объект
        self._decorate = decorate

    def draw(self):
        self._decorate.draw()


class LabelBlockDecorator(AbstractBlockDecorator):
    """ Декорирует блок текстовой меткой """
    def __init__(self, decorate: AbstractBlock, label):
        super().__init__(decorate)
        self._label = label

    def _draw_label(self):
        print(f" ... drawing label {self._label}")

    def draw(self):
        super().draw()
        self._draw_label()


class BorderBlockDecorator(AbstractBlockDecorator):
    """ Декорирует блок специальной рамкой """
    def __init__(self, decorate: AbstractBlock, border_width):
        super().__init__(decorate)
        self._border_width = border_width

    def _draw_border(self):
        print(f" ... drawing border with width {self._border_width}")

    def draw(self):
        super().draw()
        self._draw_border()


if __name__ == "__main__":
    # терминальный блок
    t_block = TerminatorBlock()

    # блок - процесс

    p_block = ProcessBlock()

    # Применим LabelDecorator к терминальному блоку

    label_decorator = LabelBlockDecorator(t_block, "Label222")

    # Применим BorderDecorator к терминальному блоку, после применения LabelDecorator

    border_decorator1 = BorderBlockDecorator(label_decorator, 22)

    # Применим BorderDecorator к блоку - процессу

    border_decorator2 = BorderBlockDecorator(p_block, 22)

    label_decorator.draw()

    border_decorator1.draw()

    border_decorator2.draw()
