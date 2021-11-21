class Phone:                                             #base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand}{self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}......."

class Smartphone(Phone):                                  #drived / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):  #all featuers of parent class avlaible in child class
        #Phone.__init__(self,brand,model_name,price)      #uncomman way to inherit 
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia','1100',1000)
smartphone = Smartphone('oneplus','5',30000,'6GB','64GB','20MP')

print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")         


