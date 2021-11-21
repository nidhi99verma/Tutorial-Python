class Mobile:
    def __init__(self,name):
        self.name = name
class MobileStore:
    def __init__(self):
        self.mobiles = []
    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New monile should be object of mobile class')
oneplus = Mobile('oneplus 6') 
samsung = 'samsung galaxy S8'                             #u can't use this if use then get error
mobostore = MobileStore()
#print(mobostore.mobiles)
#mobostore.add_mobiles(samsung)                           #type error
print(mobostore.mobiles)
mobostore.add_mobiles(oneplus)
print(mobostore.mobiles)                                  #object reference
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)                     