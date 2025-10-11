import math
class Shape:
    def area(self):
        raise NotimplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, legth, width):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        return math.pi * self.radius ** 2
