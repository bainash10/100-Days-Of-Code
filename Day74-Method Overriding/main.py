#method overriding in Python allows you to redefine a method in derived class
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
circ=Circle(5)
print(circ.area())