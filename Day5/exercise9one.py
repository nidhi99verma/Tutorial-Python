# for greater number

def greater_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
a = int(input("Enter first number : ")) 
b = int(input("Enter second number : "))  
print(greater_num(a,b))           

print(".......or......")

def greater_num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
a = int(input("Enter first number : ")) 
b = int(input("Enter second number : "))  
bigger =greater_num(a,b)
print(f"{bigger} is greater") 