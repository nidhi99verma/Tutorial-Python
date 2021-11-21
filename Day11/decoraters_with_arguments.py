#ager ek aiesa decorater bnana ho jo ji ek he decorater sy as a argument mai str,int,list ko change kre aur use decorater ko phr
#use ker only list allow or only str allow kre ....@only(...)mai argument pass ker k
from functools import wraps
def only_data_type_allow(data_type):   #nested decorater......this fun use to pass parameter
    def decorater(function):           #here we pass function as a parameter...so we can:t pass other parameter so we use one more fun(above function)
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)== data_type    for arg in args]):
                return function(*args,**kwargs)
            print("Invalid arguments")
        return wrapper
    return decorater

@only_data_type_allow(str)             #parameters --- str,int,list....
def string_only(*args):
    string = ''
    for i in args:
        string+=i
    return string
print(string_only('Nidhi','Verma','a'))                        
print(string_only('Nidhi','Verma',8))  
print(string_only('Nidhi','Verma','7'))       #because 7 in string because of this''                     

                