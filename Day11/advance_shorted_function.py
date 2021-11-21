fruits = ['mango','grapes','apple'] #list
fruits.sort()
print(fruits)
fruits1 = ('mango','grapes','apple') #tuple
print(sorted(fruits1))
#fruits1.sort()   #.....error
#fruits1.sorted() #....error
#print(fruits1)   #.....error

fruits2 = {'mango','grapes','apple'} # dict
print(sorted(fruits2))
#fruits2.sort()   #....error
#fruits2.sorted() #....error
#print(fruits2)   #.....error

print("---------------------------------------")
#short dict according to price

guitars = [
     {'Model':'Taylor 814ce','Price':450000},
    {'Model':'Yamha f310','Price':8400},
    {'Model':'Faith naptune','Price':50000},
    {'Model':'Faith apollo venus','Price':35000}
   ]
print(sorted(guitars,key=lambda d: d['Price']))
print('----------------------------------------')
print(sorted(guitars,key=lambda d: d['Price'],reverse=True))