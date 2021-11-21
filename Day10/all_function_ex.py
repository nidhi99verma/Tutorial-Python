#add all input if input in int
def my_sum(*args):
    if all([type(arg) == int or type(arg) == float    for arg in args]):#for checking all in int
        total = 0
        for num in args:
            total+= num
        return total
    else:
        return 'Wrong input'
print(my_sum(1,2,3,4.0,8.9,'Nidhi',['a','b']))    
print(my_sum(1,2,3,4.0,8.9))    
        
        