import math
class Shape:
    def area(self):
        raise NotimplementedError

class Rectangele(Shape):
    def area(self, legth, width):
        return length * width

class circle(Shape):
    def area(self, radius):
        return math.pi * radius **2
