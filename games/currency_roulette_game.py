
'''
Using the CurrencyConverter lib
https://pypi.org/project/CurrencyConverter/
'''
import time, sys, random
from currency_converter import CurrencyConverter
from score import add_score 

c = CurrencyConverter()
# usd_to_ils_ex_rate = c.convert(1, 'USD', 'ILS')
# print('USD to ILS:', usd_to_ils_ex_rate)

def play(difficulty_choice):
    # Your game logic for game 1 goes here
    print(f"\nPlaying game 'Currency Roulette' on difficulty level {difficulty_choice}")

    time.sleep(2)

# def get_money_interval(difficulty):
    usd_to_ils_ex_rate = c.convert(1, 'USD', 'ILS')
    print('1 USD is', usd_to_ils_ex_rate, 'ILS:\n', )
    # print("I am served from get_money_interval() and difficulty value is:", difficulty)
    random_amount = random.randint(1, 100)
    print(f"how much is ${random_amount} in Israeli Shekel?")
    currect_answer =  usd_to_ils_ex_rate*random_amount
    # return currect_answer



# def get_guess_from_user():
    user_answer = float(input("\nEnter your guess here: "))
    # return user_answer

# def is_list_equal(difficulty, currect_answer, user_answer):
    # Converting difficulty
    if difficulty_choice == 1:
        difficulty_parameter = 5
    elif difficulty_choice == 2:
        difficulty_parameter = 4
    elif difficulty_choice == 3:
        difficulty_parameter = 3
    elif difficulty_choice == 4:
        difficulty_parameter = 2
    elif difficulty_choice == 5:
        difficulty_parameter = 1
    else:
        print("If you read this message, surly there is an error here")

    p_up = ((100+difficulty_parameter)/100)
    p_down = ((100-difficulty_parameter)/100)
    

    if (currect_answer*p_down) <= user_answer <= (currect_answer*p_up):
            print(f"The accurate answer is", currect_answer)
            print(f"{currect_answer*p_down} <= {user_answer} <= {currect_answer*p_up}")
            print(f"You play on Level {difficulty_choice} and you win ;)")
            add_score(difficulty_choice)
    else:
            print(f"The accurate answer is", currect_answer)
            print(f"\n{currect_answer*p_down} <= {user_answer} <= {currect_answer*p_up}")
            print(f"\nYou play on Level {difficulty_choice} and you lost ;)")