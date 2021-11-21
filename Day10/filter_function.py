#filter function is itraable
def is_even(a):
    return a%2 == 0
num = [3,4,2,1,5,5,6,7,7,8,9] 
even = tuple(filter(is_even,num)) #filter(function,list or tuple)
print(even)   

#use lambda fun

even1 = tuple(filter(lambda a: a%2 == 0,num))
print(even1)

#iterable for one time but with tuple or list more then one time

even2 = filter(is_even,num)
for i in even2:
    print(i)
'''for j in even2:
    print(j)   error'''  
print("--------------")

#filter object mai ek bar he loop chala sakte hai ...ager map object ko list or tuple mai change
# ker de to ek sy jyada bar loop chala sakte hai
#more then one loops

even3 = list(filter(is_even,num))
for i in even3:
    print(i)
for j in even2:
    print(j)   

#list comprehension

new_even = [i   for i in num    if i%2 == 0]
print(even)
print(new_even)
print(list(even))
