class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price
       # self._price = price
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}.....")
    def full_name(self):
        return f"{self.brand} {self.model}"
    def send_message(self):
        pass                                        #twilio algorithm
phone1 = Phone('nokia','1100',1000)
#print(phone1._price)
#phone1._price = - 1000
#print(phone1._price)

# print(phone1.__price)            #get error

print(phone1.__dict__)           #due to above line get error so check instance variable
print(phone1._Phone__price)      #here name of instance variable change by python and add class name with instance variable     
#phone1.__price = -1000
#print(phone1.__price)            #but this not right way
phone1._Phone__price = -1000
print(phone1._Phone__price)      #her u can see __name instance variable update by same name but __name can't print show check name in dict then 