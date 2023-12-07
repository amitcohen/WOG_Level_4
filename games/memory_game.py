import time, sys, random
from score import add_score    



    
def play(difficulty_choice):

    print(f"\nPlaying game 'Memory Game' on difficulty {difficulty_choice}")
    time.sleep(2)

    # difficulty_choice
    if 1 <= difficulty_choice <= 5:
        random_list = []
        for n in range(difficulty_choice):
            random_list.append(random.randint(1, 100))
            print(random_list, end=" ")
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(0.7)
    else:
        print("Your choise is out of range")
    
    
    userlist = []
    for n in range(difficulty_choice):
        userlist.append(int(input("Insert your numbers one by one: ")))
        print("userlist", userlist) 


    if set(random_list) == set(userlist):
        print(f"\nYour guess {userlist} IS EQUAL to Random {random_list}")
        print("\nGood Job, you won the game\n")
        add_score(difficulty_choice)
    else:
        print(f"\nYour guess {userlist} is NOT EQUAL to Random {random_list}")
        print("\nOhhh, you have lost this time, Keep practice\n")

