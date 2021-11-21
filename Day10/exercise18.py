#define a function that take two argument
# 1)list containing string
# 2)string that want to find in your list and this function will return the index of string
# in your list and if statement is not present then return -1
name = ['Nidhi','Ajai','Verma']
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
        return -1
print(find_pos(name,'Nidhi')) 
print(find_pos(name,'i'))        
#itrable jis mai hum loop chala sakte hai