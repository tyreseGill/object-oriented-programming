import random

# Resolve import for check_input.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from shared.check_input import get_int_range, get_yes_no


def setup_round(bets_made: int, money_left: int) -> int:
    """
    Randomly selects the location of the queen card and prints stats.

    Returns:
        int: The index of the actual card (1, 2, or 3).
    """
    actual_card_index = random.randint(1, 3)

    print('Bets made:', bets_made)
    print('Money left: $' + str(money_left))

    return actual_card_index


def print_card_locations(actual_card_index: int):
    """
    Prints the locations of the cards based on the actual card index.

    Args:
        actual_card_index: The index of the actual card (1, 2, or 3).
    """
    print()

    if actual_card_index == 1:
        print('\t\t+-----+ +-----+ +-----+')
        print('\t\t|     | |     | |     |')
        print('\t\t|  Q  | |  K  | |  K  |')
        print('\t\t|     | |     | |     |')
        print('\t\t+-----+ +-----+ +-----+')
    elif actual_card_index == 2:
        print('\t\t+-----+ +-----+ +-----+')
        print('\t\t|     | |     | |     |')
        print('\t\t|  K  | |  Q  | |  K  |')
        print('\t\t|     | |     | |     |')
        print('\t\t+-----+ +-----+ +-----+')
    else:
        print('\t\t+-----+ +-----+ +-----+')
        print('\t\t|     | |     | |     |')
        print('\t\t|  K  | |  K  | |  Q  |')
        print('\t\t|     | |     | |     |')
        print('\t\t+-----+ +-----+ +-----+')

    print()


def check_guess(guessed_card_index: int, actual_card_index: int, money_bet: int, money_left: int) -> int:
    """
    Checks if the guessed card index matches the actual card index and updates the money left accordingly.

    Args:
        guessed_card_index: The index of the guessed card (1, 2, or 3).
        actual_card_index: The index of the actual card (1, 2, or 3).
        money_bet: The amount of money bet.
        money_left: The amount of money left.
    
    Returns:
        int: The updated amount of money left after checking the guess.
    """
    print('Card Chosen:', guessed_card_index, 'vs Queen Card:', actual_card_index)

    print_card_locations(actual_card_index)

    if guessed_card_index == actual_card_index:
        money_left += money_bet
        print('\nYou won this round but we will get you next time!')
        print('You gained', '$' + str(money_bet) + '!')

    else:
        money_left -= money_bet
        print("Oops... looks like you chose the wrong card. Maybe next time!")
        print("You lost", '$' + str(money_bet) + '!')
        
    return money_left


def check_game_over(money_left: int, play_another_round: bool) -> bool:
    """
    Checks if the game is over based on the amount of money left and whether the player wants to play another round.

    Args:
        money_left: The amount of money left.
        play_another_round: A boolean indicating if the player wants to play another round.
    
    Returns:
        bool: True if the player wants to play another round or if they have money left, False otherwise.
    """
    if money_left == 0:
        print("\nWhoops... looks like you've run out of money!")
        return False
    else:
        print('\n==============================================================\n')
        return get_yes_no('Care to play again? (Y/N): ')


def main():
    play_another_round: bool = True
    money_left: int = 100
    bets_made: int = 0

    print('====================== Three card Monte ======================\n')
    print('\t\tFind the queen to double your bet!')
    print('\n==============================================================\n')

    print('\nYou have $100.')

    while play_another_round:
        actual_card_index: int = setup_round(bets_made, money_left)
        print('\n==============================================================\n')
        money_bet: int = get_int_range('How much do you want to bet? $', 1, money_left)
        print('\n==============================================================\n')

        print('\t\t+-----+ +-----+ +-----+')
        print('\t\t|     | |     | |     |')
        print('\t\t|  1  | |  2  | |  3  |')
        print('\t\t|     | |     | |     |')
        print('\t\t+-----+ +-----+ +-----+')

        print('\n==============================================================\n')
        guessed_card_index: int = get_int_range('Guess the location of the queen: ', 1, 3)
        print('\n==============================================================\n')

        money_left = check_guess(guessed_card_index, actual_card_index, money_bet, money_left)
        play_another_round = check_game_over(money_left, play_another_round)
        print('\n==============================================================\n')

        bets_made += 1

    print('Scram punk!\n')


if __name__ == "__main__":
    main()
