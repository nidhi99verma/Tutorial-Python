#ager hum kese class mai uske sub class mai ager paticular koie function define na ho to error aae
class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        raise NotImplementedError("You have to define this mwthod in sub class")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):                        #without this get error
        return 'bhow bhow'
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):                        #without this get error
        return 'meao meao'     
doggy = Dog('boony','pug')
print(doggy.sound())               