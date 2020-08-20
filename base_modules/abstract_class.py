#!/usr/bin/env python3

# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod


# Inheriting from ABC indicates that this is an abstract base class
# Abstract classes can't be instantiated themselves
# g = GraphicShape() # this will error

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calc_area(self):
        return self.side * self.side


if __name__ == "__main__":
    c = Circle(10)
    print(c.calc_area())
    s = Square(12)
    print(s.calc_area())
