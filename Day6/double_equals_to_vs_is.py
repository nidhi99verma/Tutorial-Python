#is check memory of list ...if same then true 
fruits1 = ['orange','apple','pear']
fruits2 = ['orange','apple','pear']
fruits3 = ['banana','kiwi','apple','banana']
print(fruits1 == fruits3) 
print(fruits1 == fruits2)
print(fruits1 is fruits2)   #false: because place of memory are diffrent 