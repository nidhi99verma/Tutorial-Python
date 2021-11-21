#define a function in which pass one parameter is normal and other is (tuple or list) iterable
#first paramete value decide power(cube,square) on second parameter
#if user did't pass any args then give a user a msg 'hey u did't pass args'
#use list comprehension
def to_power(num,*args):
    if args:            #if len(args)>0:
        return[i**num   for i in args]
    else:
        return"You did't pass any args"
num = [1,2,3,4,5]
print(to_power(3,*num))            