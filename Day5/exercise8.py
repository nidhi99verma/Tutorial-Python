import random
win_num = int(random.randint(1,100))
guess_time = 1
game_over = False
user_num = int(input("Guess a number between 1 to 100 : "))
while not game_over:
    if user_num == win_num:
        print(f"You win and you guess this number in {guess_time} time")
        game_over = True
    else:
        if user_num < win_num:
            print("Too Low")
            guess_time += 1
            user_num = int(input("Guess again :"))
        else :
            print("Too High")
            guess_time += 1
            user_num = int(input("Guess again :"))         