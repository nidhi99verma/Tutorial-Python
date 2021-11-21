def multiply_nums(num,*args):
    multiply = 1
    print(num)
    print(args)   #tuple   
    for i in args:
        multiply *=i
    return multiply      
print(multiply_nums(8,1,2,3,4))  
print(multiply_nums(8))    #not get error nums value present but args not present 
#print(multiply_nums())    #get error due to nums