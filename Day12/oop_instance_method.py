#self made method call instance method
class Person:
    def __init__ (self,first_name,last_name,age):
        self.first = first_name
        self.last = last_name
        self.age = age
    def full_name(self):          #instance method
        return f'{self.first}  {self.last}'
p1 = Person('Nidhi','Verma',25)
p2 = Person('Om','Verma',15)
print(p1.first)                   # object.instance variable
print(p1.full_name())             # need to call like function ()
print(p2.full_name())             # object.instance method
#print(Person.full_name(p1))      # one more way

print("------------------------------------------------------------------")
#here l is object of list class and clear is method of list class....too many method of list class ex:pop,sort,..etc
l = [1,2,3,4]
l.clear()                 #line19
print(l)
l.append(12)
list.clear(l)            #line 19 this same..........like above line 14,line 13
print(l)
list.append(l,10)        #line 24
print(l)
l.append(20)            #line 24 this same.....same thing but different way to write
print(l)
