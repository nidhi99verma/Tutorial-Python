#init method is already a constructor but one more way ...in this we can create own constructor with help of class method
class Person:
    count_instance = 0
    def __init__ (self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod                                          #this is also class method but work as constructor
    def from_string(cls,string):
        fist_name,last_name,age = string.split(',')   
        return cls(fist_name,last_name,age)               #object
    @classmethod                                          #this is-class method
    def count_instances(cls):                             #in this method first argument pass for class
        return f'You have created {cls.count_instance} instance of {cls.__name__} class'
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def is_above_18(self):
        return self.age>18
p1 = Person('Nidhi','Verma',25) 
p2 = Person('Om','Verma',15)    
p3 = Person.from_string('Ram,Verma,5')                    #here we use constructor method so we pass only collective argumemt
print(p3.full_name())