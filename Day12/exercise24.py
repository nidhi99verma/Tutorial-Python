#make a function to count object
class Person:
    count_instance = 0
    def __init__ (self,first_name,last_name,age):
        Person.count_instance+=1
        self.first = first_name
        self.last = last_name
        self.age = age
p1 = Person('Nidhi','Verma',25)
p2 = Person('Om','Verma',15)
p3 = Person('Ram','Verma',5)
print(Person.count_instance)