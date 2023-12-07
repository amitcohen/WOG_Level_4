'''
A package that is in charge of managing the scores file. The scores file at this point will consist of
only a number. That number is the accumulation of the winnings of the user. Amount of points for
winning a game is as follows: POINTS_OF_WINNING = (DIFFICULTY X 3) + 5 Each time the user is
winning a game, the points he one will be added to his current amount of point saved in a file
'''
# games/scores.txt
# Functions
# import importlib
# from app import game_module, difficulty_choice
def add_score(difficulty_choice):
    POINTS_OF_WINNING = (difficulty_choice * 3) + 5
    print('POINTS_OF_WINNING:', POINTS_OF_WINNING)
    
    # Save POINTS_OF_WINNING to the text file
    with open('static/scores.txt', 'a') as file:
        file.write(str(POINTS_OF_WINNING) + '\n')

    # Calculate total scores
    total_scores = 0
    with open('static/scores.txt', 'r') as file:
        for line in file:
            total_scores += int(line.strip())

    print('Total Scores:', total_scores)


