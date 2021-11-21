#enhance the functionality of functions by useing decorators(decorators function)
def fun1():
    print('This is function1')
def fun2():
    print('This is function2')
fun1()
fun2()    
print("---------------------------------")
#but i want to enhance fun1 and fun2 by adding line "This is awesome function"
#before fun1 $ fun2 print anything 

#decorators_function use to enhance functionality of function fun1 $ fun2

def decorators_function(any_function): #any_function in pass any function
    def wrapper_fuction():
        print("This is awesome function")
        any_function()
    return wrapper_fuction    

def func1():
    print('This is function_1')
def func2():
    print('This is function_2')
func1 = decorators_function(func1)    #here we can use any name var =  decorators_function(func1)  
func1()                              
func2 = decorators_function(func2)
func2()        
print("----------------------------------")

#Syntactic sugar...use @ for decorator ......shortcut

@decorators_function
def function1():
    print('This is function-1')
function1()    
@decorators_function    
def function2():
    print('This is function-2')
function2()
