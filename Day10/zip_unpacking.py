#zip unpacking using *operater ---->too many way to seprate zip
#1
l = [(1,3),(2,5),(4,7),(6,9)]
print(list(zip(*l)))
#print(zip(*l))
l1,l2 = list(zip(*l))
print(l1)
print(l2)

print("------------------")

l3 = [1,2,9,4]
l4 = [5,6,7,8]
new_list = []
for pair in zip(l3,l4):
    new_list.append(max(pair))
print(new_list)    