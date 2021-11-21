def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func          #()need to access this function
var = outer_func()             #now var...outer function
var()                          #can't access without ()

def outer_func1():
    def inner_func1():
        print('inside inner func')
    return inner_func1()        #now inner_func1 have () so...no need () to use this to access function
var = outer_func1()             #now we access var without ()

def outer_func2(msg):
    def inner_func2():
        print(f'message is {msg}')
    return inner_func2         
var = outer_func2('hello there!')           
var()                        