#we can use @property decorater as getter() & making setter() by using function name in getter dot setter()
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = max(price,0)   #for not getting any negative value

    @property
    def complete_specification(self):
        return f'{self.brand}{self.model} & price is {self.__price}'

    @property                                #getter
    def price(self):
        return self.__price

    @price.setter                            #setter
    def price(self,new_price):  
        self.price = max(new_price,0)      

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand} {self.model}"

phone1 = Phone('Nokia','1100',1000)
phone1.__price = 500                                                    #update value
print(phone1.__price)
print(phone1.complete_specification)
#but still we can set negative value using __price but now atleast we have a better way to set value through setter and getter

    