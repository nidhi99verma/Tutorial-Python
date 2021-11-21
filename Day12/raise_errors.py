def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError("OOPs you are passing wrong data type to function") #TypeError u can change name
print(add('2','3'))                                                     #string    