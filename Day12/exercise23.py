#same like exercise 22 but add one more feture by define a function that apply discount call by object and pass % of discount and return price
#after discount
class Laptop:
    def __init__ (self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name
    def apply_discount(self,num):                      #instance method
        off_price = (num/100)*self.price
        return self.price - off_price
laptop1 = Laptop('hp','au114tx',63000) 
laptop2 = Laptop('Apple','Mac book',150000)
print(laptop1.apply_discount(5))
print(laptop2.apply_discount(10))                     # method in pass argument
