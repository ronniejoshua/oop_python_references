#!/usr/bin/env python3

# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class JSONify(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def to_json(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return f"{{ \"Circle\": {str(self.calc_area())} }}"


if __name__ == "__main__":
    c = Circle(10)
    print(c.calc_area())
    print(c.to_json())
