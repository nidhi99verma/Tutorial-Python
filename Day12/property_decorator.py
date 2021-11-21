#if u use property decorater then u do't need to use () so u can use this propert decorater method as avriable
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = max(price,0)   #for not getting any negative value
        #if price > 0:
        #    self.__price = price  
        #else:
        #   self._price = 0
        # self.complete_specification = f'{self.brand}{self.model} & price is {self._price}'  # if we use this variable here then we can't update value

    @property
    def complete_specification(self):
        return f'{self.brand}{self.model} & price is {self.__price}'    #this property method update __price value..when we update in obj
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}.....")
    def full_name(self):
        return f"{self.brand} {self.model}"
phone1 = Phone('Nokia','1100',1000)
phone1.__price = 500                                                    #update value
print(phone1.__price)
print(phone1.complete_specification)
#print(phone1.complete_specification())        
    