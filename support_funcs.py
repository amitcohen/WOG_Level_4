from app import start_play
from utils import screen_cleaner


def play_again():
    while True:
        pa = input("\nWould you like to continue playing? Y / N: ").strip().upper()
        if pa == 'Y':
            screen_cleaner()
            # welcome()  # You may want to include this line, but it's commented out in your code
            start_play()
        elif pa == 'N':
            print('\nBye bye')
            break
        else:
            print("Error! Please enter 'Y' or 'N'")

        