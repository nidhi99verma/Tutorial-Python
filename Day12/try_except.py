#try except ka use exception ko handle kerne k leya kerte h 
#ager exception ka real name use hre to performance per firk deakta hai...jalde execute hoga
#we can use more than one exception to handle error
while True:
    try:
        age = int(input('enter Your age :'))
        break
    except ValueError:                                    #value exception handle
        print("may be you entered string insted of number,try again")
    except :                                              #other exception
        print("Unexpected error..")
if age < 18:
    print("You can not play this game")
else:
    print("You can play this game")
                    