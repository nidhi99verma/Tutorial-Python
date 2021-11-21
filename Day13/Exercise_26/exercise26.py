#salary.txt folde from read and write in output folder
with open('salary.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary}')