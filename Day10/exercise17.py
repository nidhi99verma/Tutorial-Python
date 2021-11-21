#define a function which take list in input and return a list with capital latter of first
#char and string in reverse if print(func(name,reverse_str = True))
def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return[name[::-1].title()  for name in l]
    else:
        return[name.title()   for name in l]
names = ['Nidhi','Verma']
print(func(names,reverse_str = True))
#print(func(names))        