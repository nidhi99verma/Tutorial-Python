def multiply_nums(*args): #hear args is parameters
    multiply = 1
    for i in args:
        multiply *=i
    return multiply
print(multiply_nums())    
print(multiply_nums(1,2,3,4))    #hera 1,2,3,4 is arguments    