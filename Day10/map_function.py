#map function is itraable....map fun that it gives an list like iterable object and we can
#itrate through it
num = [1,2,3,4,5]
def square(a):
    return a**2
squares = list(map(square,num)) #map(function name,list or tuple)
print(squares)    

#in lamdba function

squares1 = list(map(lambda a:a**2,num)) 
print(squares1)    

#in list comprehension

squares2 = [i**2 for i in num]
print(squares2)    

#without map,lambda and comprehension

new_list = []
def square3(b):
    return b**2
for i in num:
    new_list.append(square3(i))
print(new_list)        