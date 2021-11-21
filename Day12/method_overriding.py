#if we check full_name of flash class without 3rd update then we get 2nd full_name value
class Phone:  
                                               #base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand}{self.model_name}"
        
    def make_a_call(self,number):
        return f"calling {number}......."

class Smartphone(Phone):     
                                 #drived class / child class & base class/ parent class both
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):  #all featuers of parent class avlaible in child class
        #Phone.__init__(self,brand,model_name,price)      #uncomman way to inherit 
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
        
    def full_name(self):                                                              # 2nd time update
        return f"{self.brand}{self.model_name} & price is {self._price}"

class FlagshipPhone(Smartphone):  
                             #drived class / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera
                                                               
    def full_name(self):                                                              #3rd time update
        return f"{self.brand}{self.model_name} and price is {self._price} and front camera {self.front_camera}"

phone = Phone('nokia','1100',1000)
smartphone = Smartphone('oneplus','5',30000,'6GB','64GB','20MP')
fs = FlagshipPhone('oneplus','7T',40000,'10GB','225GB','30MP','20MP')

print(fs.full_name())
print(smartphone.full_name())
print(help(FlagshipPhone))
print(help(Smartphone))