#print first char of all items in list
#list comprehension

names = ['Nidhi','Ajai','Verma']
new_list1 = [name[0]    for name in names]
print(new_list1)

#simple way

new_list = []
for names in names:
    new_list.append(names[0])
print(new_list)    