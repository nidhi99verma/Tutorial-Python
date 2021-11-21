#print a list which turn even no*2 and odd no*(-1)
#simple way

nums = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i**2)
    else:
        new_list.append(-i)
print(new_list)      

#comprehension [append part   if condition   else condition    for loop part]

nums = [1,2,3,4,5,6,7,8,9,10]
new_list = [i**2  if(i%2 == 0)   else -i    for i in nums]
print(new_list)
