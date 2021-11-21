def decorators_function(any_function): 
    def wrapper_fuction():
        print("This is awesome function")
        any_function()
    return wrapper_fuction    

@decorators_function
def func(a):
    print(f'This is function with argument {a}')   
#func(5)    

#getting error because decorator_function(func)in pass argument but in func(a) in pass a and
#in decorator_function in function wrapper_function in not pass any argument..so we get error
#after decorators_function ,func dependent on wrapper function and in this function pass no argument 

#improve

def decorators_functions(any_function): 
    def wrapper_fuction(*args,**kwargs):     #now pass paramer
        print("This is awesome function....")
        any_function(*args,**kwargs)
    return wrapper_fuction    

@decorators_functions
def fun(a):
    print(f'This is function with argument {a}')
fun(2)
#@decorators_functions
#def add(a,b):
#    return a+b
#add(2,6)
#print(add(2,6))
#get error because wrapper_function does't return any thing so we get error
print("---------------------------")

#improve

def decorators_functions1(any_function): 
    def wrapper_fuction(*args,**kwargs):     
        print("This is awesome function....")
        return any_function(*args,**kwargs)
    return wrapper_fuction    

@decorators_functions1
def fun1(a):
    print(f'This is function with argument {a}')
fun1(2)
@decorators_functions1
def add(a,b):
    return a+b
print(add(2,6))
