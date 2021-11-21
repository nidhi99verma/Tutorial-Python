#this sequece follow rule to give any any parameter(PADK)
#1)noemal parameter
#2)*args
#3)default parameters
#4)**kwargs

def func(name,*args,last_name = 'Unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Nidhi',1,2,3,4,a = 1,b = 2)    