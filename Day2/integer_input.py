num_one = int(input("enter 1 number ")) #if we does't use int then my input treat like string....ex: 4
num_two = int(input("enter 2 number ")) #5
total = num_one + num_two               #without int get 45 outpout
print("Total is "+str(total))          #if we does't use str before total then get error because "Total is " string and total is integer 
                                        #and we can't add integer and string 