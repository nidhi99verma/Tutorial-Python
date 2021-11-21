num = [1,2,3,4,5]  #itrables---->tuples,list,str
square = map(lambda a:a**2 ,num) #iterator
print(square)
for i in square:             #print(next(square))
    print(i)                 #print(next(num))
print("---------------")
#how to work for loop
'''step1: call item fun
step2 :iter (number)--->iterator
step3 :net(iter(number))  

ex:'''

number_iter = iter(num)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
#print(next(number_iter)) error
