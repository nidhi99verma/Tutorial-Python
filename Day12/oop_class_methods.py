#class method ka kam use kerte hai ...instance method jyda use kerte hai
#class method mai phle argument class k leya pass kerte hai aur @classmethod decorater use kerte hai
class Person:
    count_instance = 0
    def __init__ (self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod                                                 #this is class method
    def count_instances(cls):                                    #in this method first argument pass for class
        return f'You have created {cls.count_instance} instance of {cls.__name__} class'
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Nidhi','Verma',25) 
p1 = Person('Om','Verma',15)          
print(Person.count_instances())
#print(p1.count_instance())
      