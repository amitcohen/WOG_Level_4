def welcome():
    name = input(str('Please enter your name: '))
    print()
    print(f'Hi {name.capitalize()} and welcome to the World of Games: The Epic Journey\n')


import importlib

def start_play():
    game_choices = {1: 'memory_game', 2: 'Guess Game', 3: 'Currency Roulette'}

    # Display the available game choices
    print("Choose a game to play:")
    for choice, description in game_choices.items():
        print(f"{choice}: {description}")

    # Get the game choice from the user
    game_choice = input("Enter the number of the game you want to play: ")

    try:
        game_choice = int(game_choice)
        if game_choice not in game_choices:
            print("Invalid game choice.")
            return
    except ValueError:
        print("\nInvalid input. Please enter a valid game number.")
        return

    # Get the difficulty level from the user
    difficulty_choices = {1: 'Very Easy', 2: 'Easy', 3: 'Intermediate', 4: 'Hard', 5: 'Very Hard'}
    
    # Display the available game difficulties
    print("\nChoose a game difficulty:")
    for d_choice, d_description in difficulty_choices.items():
        print(f"{d_choice}: {d_description}")

    difficulty_choice = input("Choose the difficulty (1, 2, 3, 4, or 5): ")

    # Dynamically import the selected game module from the 'games' folder
    game_module_name = f"games.{game_choices[game_choice]}"
    try:
        game_module = importlib.import_module(game_module_name)
    except ModuleNotFoundError:
        print(f"Error: The selected game module '{game_module_name}' does not exist.")
        return

    # Call the play() function from the selected game module and pass the difficulty
    game_module.play(int(difficulty_choice))
    return

