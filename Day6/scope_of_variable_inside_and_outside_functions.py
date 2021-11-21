x = 5               #Global Variable
def func():
    global x        #without 'global' we can't acess first x
    x = 7           #Local Variable
    return x
print(x)
print(func())       #after func value of x=5 update value of x
print(x)    