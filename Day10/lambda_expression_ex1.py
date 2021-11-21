#without lambda function
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False
print(is_even(4))            
#with lambda function
is_even1 = lambda a:a%2 == 0
print(is_even1(5))