#use class variable ....class name . variable name which right but if we try to update this class variable for paticular object then we can't get right output
#so .....need to use object(self).class variable
class Laptop:
    discount_percent = 10                                   #class variable
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name
    def apply_discount(self):                                #instance method
        off_price = (Laptop.discount_percent/100)*self.price                                  #this is not right code
        return self.price - off_price

#Laptop.discount_percent = 100        
laptop1 = Laptop('hp','au114tx',63000) 
laptop2 = Laptop('Apple','Mac book',150000)
print(laptop1.apply_discount())
print(laptop2.apply_discount())                                #object.instance method
print('---------------------------------------------------')
laptop1.discount_percent = 50                                #if off_price = (Laptop.discount_percent/100)*self.price use this then not get right output
print(laptop1.__dict__)                                      #because we update class varible in particular object(laptiop1)so above use not laptop...use self
print(laptop1.apply_discount())

#if u want to update any class variable time to time for any object then use self with variable or if u want to update for all object 
#then u can use class.varriable name

#her we use self.class variable because update class varriable for particular object (laptop1)

class Laptop:
    discount_percent = 10                                   #class variable
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name
    def apply_discount(self):                                #instance method
        off_price = (self.discount_percent/100)*self.price                        # this is right code
        return self.price - off_price

#Laptop.discount_percent = 100        
laptop1 = Laptop('hp','au114tx',63000) 
laptop2 = Laptop('Apple','Mac book',150000)
print(laptop1.apply_discount())
print(laptop2.apply_discount())                                #object.instance method
print('---------------------------------------------------')
laptop1.discount_percent = 50                                #if off_price = (Laptop.discount_percent/100)*self.price use this then not get right output
print(laptop1.__dict__)                                      #because we update class varible in particular object(laptiop1)so above use not laptop...use self
print(laptop1.apply_discount())
#here dict show that one mere item add in arrgument ....discount_percentclear