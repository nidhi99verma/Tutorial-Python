names = ['abc','abcd','abcde']
length = map(len,names) # map object
for i in length:        #map object mai ek he bar loop chala sakte hai
    print(i)
'''for j in length:
      print(j)'''
print("..............................")
#map object mai ek bar he loop chala sakte hai ...ager map object ko list or tuple mai change
# ker de to ek sy jyada bar loop chala sakte hai

#more then one loops

length = list(map(len,names)) #because of list here both loop run
for i in length:        
    print(i)
for j in length:
      print(j)
