#use of min and max fun according to character of items not onlyn on value
num = [1,3,4,6]
print(min(num))  #min accordin value

print("--------------")

name = ['Nidhi','Ajai','Verma']
def fun(items):
    return len(items)
print(min(name,key = fun)) #min or max(list or tuple name , key = function name)
print(max(name,key = fun))    

print("-----------------")

names = ['Nidhi','Verma','Ajai']
print(max(names,key = lambda item:len(item)))
print(min(names,key = lambda item:len(item)))