#import random
#win_num = random.randint(0,100)
win_num = 50
guess_num = int(input("Enter number between 0 to 100: "))
if win_num == guess_num:
    print("You Win")
else:
    if guess_num > win_num :
        print("To high")
    if guess_num<win_num:          #else:    
        print("To low")   