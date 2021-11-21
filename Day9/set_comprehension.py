#print a set in which squares of numbers
#{items of set   for loop}

s = {k**2   for k in range(1,11)}
print(s)

#ex:2

names = ['Nidhi','Ajai','Verma']
first = {name[0]    for name in names}
print(first)