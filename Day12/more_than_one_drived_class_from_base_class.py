class Phone:                                             #base class/ parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand}{self.model_name}"
        
    def make_a_call(self,number):
        return f"calling {number}......."

class Smartphone(Phone):                                  #drived class / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):  #all featuers of parent class avlaible in child class
        #Phone.__init__(self,brand,model_name,price)      #uncomman way to inherit 
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class Smartphone2(Phone):                                #drived class / child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera       

phone = Phone('nokia','1100',1000)
#smartphone = Smartphone('oneplus','5',30000,'6GB','64GB','20MP')
smartphone = Smartphone2('oneplus','6T',35000,'8GB','64GB','25MP')

print(smartphone.full_name())