import math


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*math.pi
    
    def perimeter(self):
        return 2*self.radius*math.pi


if __name__== "__main__":
    c1 = Circle(10)
    print(c1.area())
    print(c1.perimeter())
