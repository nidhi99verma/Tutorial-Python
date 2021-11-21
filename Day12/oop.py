class Person:                                      #class name Person   
    def __init__(self,first_name,last_name,age):   #init function is constructer(self or any first attribute represent to object,.......->attributes)
        print("Init Method called")                # line3
        self.first_name = first_name               #instance variable
        self.last_name = last_name                 #instance variable
        self.noo_age = age                                #instance variable
p1 = Person('Nidhi','Verma',25)                    #p1 object....>call 2 line ...so everytime when object inetialized then call constructer
p2 = Person('Ram','Verma',15)                      #p2 object....>so line3 show constructer call
print(p1.first_name)                               #object  and instance both same
print(p1.last_name)
print(p1.noo_age)        
print(p2.first_name)
print(p2.last_name)
print(p2.noo_age)        
