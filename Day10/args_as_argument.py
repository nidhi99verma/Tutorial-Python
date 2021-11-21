def multiply_nums(*args): 
    multiply = 1
    for i in args:
        multiply *=i
    return multiply
num = [1,2,3,4] # this is list but same for tuples......hear 1,2,3,4 is arguments
print(multiply_nums(*num)) #unpacked list.....because use of *
#print(multiply_nums(num)) #only num list in we can't multiply because this list is packed