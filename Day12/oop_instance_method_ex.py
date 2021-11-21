class Person:
    def __init__ (self,first_name,last_name,age):
        self.first = first_name
        self.last = last_name
        self.age = age
    def is_above(self):          #instance method
        return self.age>18       #or if self.age>18:
                                 #       return True  
p1 = Person('Nidhi','Verma',25)
p2 = Person('Om','Verma',15)
print(p1.first)                  
print(p1.is_above()) 
print(p2.last)                  
print(p2.is_above())   