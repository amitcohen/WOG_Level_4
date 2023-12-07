import time, sys, random
from score import add_score

def play(difficulty_choice):
    # Your game logic for game 1 goes here
    print(f"\nPlaying game 'Guess Game' on difficulty {difficulty_choice}")

    time.sleep(2)
    

    if 1 <= difficulty_choice <= 5:
            range_start = 10**(difficulty_choice-1)
            range_end = (10**difficulty_choice)-1
            gen_num = random.randint(range_start, range_end)
            print(gen_num, end=" ")
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(0.7)
    else:
        print("Ilegal number, try again")
    

    try:
        user_guess = int(input('Enter your guess here: '))
    except ValueError:
        print("Invalid input. Please enter a valid number.")


    if user_guess == gen_num:
        print(f"\nYour guess {user_guess} IS EQUAL to Random {gen_num}")
        print("Good Job, you won the game\n")
        add_score(difficulty_choice)
    else:
        print(f"\nYour guess {user_guess} is NOT EQUAL to Random {gen_num}")
        print("Sorry, you have lost this time, Keep practice\n")
