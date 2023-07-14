"""
Dependencies: pip install random
"""

import random

# Add type hinting '-> int'
def guess_number(low: int = 1, high: int = 100) -> int:
    """
    Plays a guessing game where the user must guess a random number between low and high. Returns the randomly generated number.

    Parameters:
        low (int) : The lowest possible in the range (default 1).
        high (int): The highest possible number in the range (default 10).

    Return:
        int: The randomly generated number.
    """
    random_num = random.randint(low, high)
    user_guess = None

    while user_guess != random_num:
        user_guess = int(input(f'Guess a number between {low} and {high}: '))
        if user_guess < random_num:
            print('Your guess is too low. Try again!')
        elif user_guess > random_num:
            print('Your guess is too high. Try again!')
        else:
            print('Congratulations, you guessed the number correctly!')

    return random_num

random_num = guess_number(10,20)
print(f'The randomly generated number was {random_num}.')
