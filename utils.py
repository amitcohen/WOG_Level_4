# Variables
'''SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”'''
# SCORES_FILE_NAME

'''BAD_RETURN_CODE - A number representing a bad return code for a function.'''
# BAD_RETURN_CODE

# Functions
'''Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).'''
def screen_cleaner():
    import os
    import platform
    import time
    # time.sleep(1)
    if platform.system() == "Windows":
        time.sleep(2)
        os.system("cls")
    else:
        time.sleep(2)
        os.system("clear")

screen_cleaner()