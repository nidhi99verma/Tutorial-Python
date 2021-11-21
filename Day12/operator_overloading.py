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

    def __add__(self,other):
        return self.price + other.price    



my_phone_a = Phone2('nokia','1100',1000)
my_phone_b = Phone2('nokia','1600',2000)
print(my_phone_a + my_phone_b)
#print(my_phone_a + my_phone_b)


