age = int(input("Please enter your age : "))
if  0<=age<=3:
    print("Ticket price : Free ")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")        