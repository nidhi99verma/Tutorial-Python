#without lambda function
def func(s):
    if len(s)>5:
        return True
    else:
        return False
print(func("abcdef"))        
#with lambda function---->lambda:return if ka   if condition  else condition 
func1 = lambda s:True    if len(s)>5 else False
print(func1("cdef")) 
#or
func2 = lambda s:len(s)>5 
print(func2("ghijk")) 