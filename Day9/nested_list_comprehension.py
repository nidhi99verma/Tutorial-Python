#print nested list [[1,2,3],[1,2,3],[1,2,3]]
#simple way

new_list = []
for j in range(3):
    new_list.append([1,2,3]) 
print(new_list)    

#comprehension way

nested_comp = [[i   for i in range(1,4)]    for j in range(3)]    #range(1,4)....range(0,3)
print(nested_comp)