with open('file7.txt','r') as rf:
    with open('file8.txt','w') as wf:
        wf.write(rf.read())