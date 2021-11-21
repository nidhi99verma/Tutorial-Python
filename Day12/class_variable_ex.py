class Laptop:
    discount_percent = 10                                   #class variable
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name
    def apply_discount(self):                                #instance method
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price
laptop1 = Laptop('hp','au114tx',63000) 
laptop2 = Laptop('Apple','Mac book',150000)
print(laptop1.apply_discount())
print(laptop2.apply_discount())                                #object.instance method