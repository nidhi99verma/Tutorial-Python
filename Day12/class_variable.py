class Circle:
    pi = 3.14                               #this is class variable
    def __init__ (self,radius):
        self.radius = radius
    def calcu_circumference(self):
        return 2*Circle.pi*self.radius      #class variable use ....class name dot variable name(not self)
c1 = Circle(4)
c2 = Circle(5)
print(c1.calcu_circumference())
            