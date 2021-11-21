#kise b chez ko ek sy jyada form hona (many form) ex : 2+3 = 5,'abc'+'def'= 'abcdef' here + is polymorphism because + work for both add int and add string
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

class SmartPhone(Phone2):

    def __init__(self,brand,model,price,camera):
        super().__init__(brand,model,price)
        self.camera = camera

    def phone_name(self):                                             #again
        return f'{self.brand}{self.model}  and price is {self.price}'     

    def __len__(self):                                                #again
        return self.price    

my_phone_a = Phone2('nokia','1100',1000)
my_phone_b = Phone2('nokia','1600',2000)
my_phone_s = SmartPhone('onePlus','5t',33000,'16MP')

print(my_phone_s.phone_name())
print(my_phone_a.phone_name())
print(len(my_phone_s))
print(len(my_phone_a))

#here phone_name and len use for more then one obj
