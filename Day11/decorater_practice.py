#make a decorater that allow only integer
from functools import wraps                 
def only_int_allow(function): 
    @wraps(function)                     
    def wrapper(*args,**kwargs):  
        if all ([type(arg)== int    for arg in args]):   #with comprehension
            return function(*args,**kwargs) 
        print("Invalid argument")
       #data_types = []                                  #without comprehension
       #for arg in args:
       #    data_types.append(type(args)==int)
       #if all(data_types):
       #    return function(*args,**kwargs)
       #else:
       #    print("Invalid arguments")
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total
#print(add_all(1,2,3,4,5,[1,2,3]))
print(add_all(1,2,3,4,5,5))        