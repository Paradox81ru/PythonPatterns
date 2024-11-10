""" Структурный шаблон проектирования 'Мост'"' """
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self):
        raise NotImplemented

    @abstractmethod
    def render_square(self):
        raise NotImplemented


class OpenGLRenderer(Renderer):
    def render_circle(self):
        print("Drawing circle using OpenGL")

    def render_square(self):
        print("Drawing square using OpenGL")


class DirectXRenderer(Renderer):
    def render_circle(self):
        print("Drawing circle using DirectX")

    def render_square(self):
        print("Drawing square using DirectX")


class BridgeShape(ABC):
    def __init__(self, render: Renderer):
        self.render = render

    @abstractmethod
    def draw(self):
        raise NotImplemented


class Circle(BridgeShape):
    def draw(self):
        self.render.render_circle()


class Square(BridgeShape):
    def draw(self):
        self.render.render_square()

if __name__ == "__main__":
    opengl_render = OpenGLRenderer()
    directx_render = DirectXRenderer()

    circle = Circle(opengl_render)
    square = Square(directx_render)

    circle.draw()
    square.draw()