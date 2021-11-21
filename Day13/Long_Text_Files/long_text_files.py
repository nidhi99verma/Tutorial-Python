with open('fileL.txt','r') as f:
    data = f.read(100)             #data print 1st 100 char then next again...and get complet text`
    while len(data) > 0:
        print(data)
        data = f.read(100)