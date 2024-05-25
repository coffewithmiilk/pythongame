import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    clear_screen()
    print('==============================')
    print('      GUESS THE NUMBER!       ')
    print('         From 0 to 100        ')
    print('==============================\n')

    random_number = random.randint(1, 100)
    attempts = 0
    initial_points = 1050
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guessed_number = int(input('ENTER YOUR GUESS: '))
        except ValueError:
            print("\nPlease enter a valid number.\n")
            continue
        
        attempts += 1
        clear_screen()
        
        if guessed_number < random_number:
            print('==============================')
            print('          ATTEMPT             ')
            print('==============================\n')
            print('Wrong guess! The number is too low!\n')
        elif guessed_number > random_number:
            print('==============================')
            print('          ATTEMPT             ')
            print('==============================\n')
            print('Wrong guess! The number is too high!\n')
        else:
            points = initial_points - (attempts * 10)
            print('==============================')
            print('          CONGRATULATIONS!    ')
            print('==============================\n')
            print(f'You got it! The number was: {random_number}.')
            print(f'You scored {points} points with {attempts} attempts.\n')
            guessed_correctly = True

    print('==============================')
    print('         END OF GAME          ')
    print('==============================')

start_game()
