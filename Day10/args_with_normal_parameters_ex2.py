def multiply_nums(num1,num2,*args):
    multiply = 1
    print(args)   #tuple   
    for i in args:
        multiply *=i
    return multiply      
print(multiply_nums(8,9,1,2,3,4))  #num1=8 num2=9
print(multiply_nums(8,9))  #in this args value not given...if args not present no problem
#print(multiply_nums(8))   #get error due to num2
#print(multiply_nums())    #get error due to num