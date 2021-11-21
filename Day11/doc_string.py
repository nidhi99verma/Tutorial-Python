#we use triple single quates ''' or triple double quotes """ for docstring
#help use to know how to any module work
def add(a,b):
    '''This function takes 2 numbers and return thir sum'''
    return a+b
print(add.__doc__)    #add,len,sum,max,min,sorted.....
print(sum.__doc__)   
print(max.__doc__)
print(help(add))      #add,len,sum,max,min,sorted.....
print(help(sum))   
print(help(max))