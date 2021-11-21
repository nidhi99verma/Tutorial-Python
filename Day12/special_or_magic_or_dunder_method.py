class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand}{self.model}'

    def __str__(self):
        return f'{self.brand}{self.model}'                           #dunder method or special

    def __repr__(self): 
        return f'{self.brand}{self.model} and price is {self.price}' #magic method

my_phone = Phone('nokia','1100',1000)
print(my_phone)
print(str(my_phone))
print(repr(my_phone))             

#
print('----------------------------------')

class Phone1:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand}{self.model}'

    def __str__(self):
        return f'{self.brand}{self.model}  and price is {self.price}'                      #dunder method or special

    def __repr__(self): 
        return f'Phone1 (\'{self.brand}\',\'{self.model}\',\'{self.price}\')'                                                  #magic method

my_phone = Phone1('nokia','1100',1000)
print(my_phone.__repr__())
# print(str(my_phone))
# print(repr(my_phone)) 

#
print("--------------------------------------")

class Phone2:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand}{self.model}'

    def __str__(self):
        return f'{self.brand}{self.model}  and price is {self.price}'                      #dunder method or special

    def __repr__(self): 
        return f'Phone2 (\'{self.brand}\',\'{self.model}\',\'{self.price}\')'              #magic method

    def __len__(self):
        return len(self.phone_name())



my_phone = Phone2('nokia','1100',1000)
print(len(my_phone))
print(my_phone.__len__())


