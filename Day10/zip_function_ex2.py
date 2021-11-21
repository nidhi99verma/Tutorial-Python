example = [('a',1),('b',2)]
print(dict(example))

print("------------")

user_id = ['user1','user2','user3']
names = ['Nidhi','Ajai','Verma']
age = ['25','30','15']
print(list(zip(user_id,names,age)))
#print(dict(zip(user_id,names,age))) 
#errror if more then two list or tuples then can't change in dictionary