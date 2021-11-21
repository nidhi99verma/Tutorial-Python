#create a laptop class with attributes like brand_name,model_name,price...and create two object of your laptop class
class Laptop:
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.modle = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name
laptop1 = Laptop('HP','au11tx',65000)
laptop2 = Laptop('Apple','Mac book',150000)
print(laptop1.brand)
print(laptop1.modle)
print(laptop1.price)
print(laptop1.laptop_name)
print(laptop2.brand)
print(laptop2.modle)
print(laptop2.price)
print(laptop2.laptop_name)