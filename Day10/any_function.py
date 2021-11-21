#if condition true for any one items then get True and if all condition false for all item 
# then false
num = [2,4,7,8]
even = []
for no in num :
    even.append(no % 2 == 0)
print(even)    
print(any(even))      

print("-----------")

num1 = [2,4,6,8]
print(any([no % 2 == 0 for no in num1 ]))
