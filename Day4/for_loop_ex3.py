name = input("enter your name : ")
temp_var = ""
for i in range (0,len(name)):
    if name[i] not in temp_var:
        print(f"{name[i]}:{name.count(name[i])}")  
    temp_var+=name[i]  