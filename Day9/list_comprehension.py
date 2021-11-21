#comprehension reduce line of code
#---square of list
#use...list comprehension

squares = [i**2 for i in range(1,11)]    #[append part    for loop]
print(squares)

#without list comprehension same program

squares = []
for i in range(1,11):    #for loop
    squares.append(i**2) #append part
print(squares)    
