from functools import wraps                  #step:1
def decorators_functions1(any_function): 
    @wraps(any_function)                     #step:2
    def wrapper_fuction(*args,**kwargs):     
        '''This is wrapper function'''       #docstring for wrapper 
        print("This is awesome function....")
        return any_function(*args,**kwargs)
    return wrapper_fuction    

@decorators_functions1
def add(a,b):
    '''This is add function'''
    return a+b
print(add.__doc__)
print(add.__name__)
#without step:1 & step:2 when print(add.__doc__) then we get wrong docstring(docstring of wrapper)

print("------------------------------ex-----------------------------")

from functools import wraps                  
def decorators_functions2(any_function): 
    @wraps(any_function)                     
    def wrapper_fuction(*args,**kwargs):     
        '''This is wrapper function'''      
        print(f"Your are calling {any_function.__name__} function")
        print(f"{any_function.__name__}")                             #function name
        return any_function(*args,**kwargs)
    return wrapper_fuction    

@decorators_functions2
def add1(a,b):
    '''This is add function'''
    return a+b
print(add1(4,6))    

