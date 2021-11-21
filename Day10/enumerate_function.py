#enumerater function use to tracking position of our item in iterable
#without enumerater
names = ['Nidhi','Ajai','Verma']
pos = 0
for name in names:
    print(f"{pos}-----{name}")
    pos+=1
#with enumerater--->for position i in enumerater(list or tupel):
for pos,name in enumerate(names):
    print(f"{pos}-----{name}")        