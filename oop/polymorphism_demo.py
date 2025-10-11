class shape:
    def area(self):
        raise NotimplementedError

class Rectangele(shape):
    def area(self, legth, width):
        return length * width

class circle(shape):
    def area(self, radius):
        return math.pi * radius **2
