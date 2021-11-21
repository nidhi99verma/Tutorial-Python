'''zip function combinde two list or tuples in one list or tuples which have items first 
index of first list and second list's first index'''

user_id = ['user1','user2','user3']
names = ['Nidhi','Ajai','Verma']
print(list(zip(user_id,names)))
print(zip(user_id,names))     #iterater
print(tuple(zip(user_id,names)))
print(dict(zip(user_id,names)))