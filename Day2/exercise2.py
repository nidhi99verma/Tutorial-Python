num_1,num_2,num_3 = input("Please enter three number ").split(",")
avg = (int(num_1)+int(num_2)+int(num_3))/3
print(f"This is average of your three number {avg}")
print(f"This is average of your three number {(int(num_1)+int(num_2)+int(num_3))/3}")

#print(f"This is average of your three number {(int((num_1)+(num_2)+(num_3)))/3}") we can't inetialized all integer at time
#num_1,num_2,num_3 = int(input("Please enter three number ").split(","))           we can't inetialized all integer at time  
#num_1,num_2,num_3 = int(input("Please enter three number ")).split(",")           we can't inetialized all integer at time
#print(f"This is average of your three number {((num_1)+(num_2)+(num_3))/3}")      all above inetialization is wrong