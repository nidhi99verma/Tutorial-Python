# *operator use to take more then two or user dependent input items ...like list,tuples...in input
def all_total(*args):  #u can take any name in place of args
    print(args)
    print(type(args))
all_total(1,2,3,4,5,6)   #tuple    



def all_total1(*args):
    total = 0
    for num in args:
        total += num
    return total
print(all_total1(1,2,3,4,5,6))        
