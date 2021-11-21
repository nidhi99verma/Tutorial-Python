#unorderd collection of unique items....no idexing....no item repeat
s = {1,2,3,4,5,6,7,3,4,2,1}
print(s)
print("-----------------")
l = [1,2,3,5,8,4,6,2,6,2,6,7]
s1 = set(l)                         # change list into set
print(s1)
print("----------------")
s1 = list(set(l))             # s1 = list(s1)      change set into list
print(s1)