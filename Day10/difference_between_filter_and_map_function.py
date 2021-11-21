#map takes all object in a list and allows you to apply a fun to it
#filter takes all object in a list and runs that through a function to create a new list 
#with all object that return True in that fun

def f(x):
    return x%2 == 0
def m(y):
    return y*2 
list = [1,2,3,4]

flist = tuple(filter(f,list))
print(list)
print(flist)
#diff in output
mlist = tuple(map(m,list))
print(list)
print(mlist)
