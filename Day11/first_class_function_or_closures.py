def square(a):
    return a**2
s = square              #clouser
print(square(7))        #same work
print(s(7)) 
print(square.__name__)  #same function 
print(s.__name__)
print(square)           #same place in memory
print(s)
