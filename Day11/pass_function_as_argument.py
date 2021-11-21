def square(a):
    return a**2
l = [1,2,3,4]
print(list(map(square,l)))
print(list(map(lambda a: a**2,l)))    

#now pass functin

def my_map(func,l):  #now pass functin(function,itrable)
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l))        

#above both function in below one function

def my_map2(func,l):
    return[func(item)   for item in l]  #list comprehension
print(my_map2(square,l))
print(my_map2(lambda a: a**2,l))        #lambda function
 
 #now we can use this function in too many work ....if we want cub ...just change 3 or even oddd
 #so we use function in argument