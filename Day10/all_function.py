#if condition true for all items then get True either False
num = [2,4,7,8]
even = []
for no in num :
    even.append(no % 2 == 0)
print(even)    
print(all(even))      

print("-----------")

num1 = [2,4,6,8]
print(all([no % 2 == 0 for no in num1 ]))
