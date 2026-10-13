import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range, get_yes_no

import random

def main():
    # Sets up the game assuming the player has $100 and wants to play
    quit_or_play = True
    money_left = int(100)
    bets_made = 0

    # Makes sure that the game runs so long as the user has money and they've indicated that they
    # still want to play
    while money_left > 0 and (quit_or_play != False):

        # Automatically generates a random number within the range 1-3 and assigns it to the queen card
        # at the start of every round
        # A specific message is printed during the first round and another lets the player know how many
        # bets they've made and the money they have left at the start of each round
        queen_card = random.randint(1, 3)
        if bets_made == 0:
            print('-Three card Monte-')
            print('Find the queen to double your bet!')
            print('\nYou have $100.')
        print('Bets made:',bets_made)
        print('Money left: $' + str(money_left))

        # Asks the user to input an acceptable amount of money for betting and prints out a deck of
        # cards listed 1-3
        money_bet = get_int_range('How much do you want to bet? $', 1, money_left)
        print('\n+-----+ +-----+ +-----+')
        print('|     | |     | |     |')
        print('|  1  | |  2  | |  3  |')
        print('|     | |     | |     |')
        print('+-----+ +-----+ +-----+')

        # Asks the user to choose one of the 3 cards, increments the variable associated with the number
        # of bets, and compares the user's guess to the location of the Queen card
        card_chosen = get_int_range('\nFind the queen: ', 1, 3)
        bets_made += 1
        print('Card Chosen:', card_chosen, 'vs Queen Card:', queen_card)

        # Checks to see if the user guessed the location of the queen card correctly
        if int(card_chosen) == int(queen_card):
            money_left += money_bet
            print('\nYou won this round but we will get you next time!')
            print('You gained', '$' + str(money_bet) + '!')
        elif int(card_chosen) != int(queen_card):
            money_left -= money_bet
            print("Oops... looks like you chose the wrong card. Maybe next time!")
            print("You lost", '$' + str(money_bet) + '!')

        # Generates the locations of the Queen and King cards based on the randomly generated number
        # for the Queen card
        if queen_card == 1:
            print('\n+-----+ +-----+ +-----+')
            print('|     | |     | |     |')
            print('|  Q  | |  K  | |  K  |')
            print('|     | |     | |     |')
            print('+-----+ +-----+ +-----+')
        elif queen_card == 2:
            print('\n+-----+ +-----+ +-----+')
            print('|     | |     | |     |')
            print('|  K  | |  Q  | |  K  |')
            print('|     | |     | |     |')
            print('+-----+ +-----+ +-----+')
        else:
            print('\n+-----+ +-----+ +-----+')
            print('|     | |     | |     |')
            print('|  K  | |  K  | |  Q  |')
            print('|     | |     | |     |')
            print('+-----+ +-----+ +-----+')

        # Checks to make sure that the user still has money to play another game
        # If not, the user is forcibly exited from the game
        if money_left == 0:
            print("Whoops... looks like you've run out of money!")
            break

        # Asks the user if they want to play again
        # If the user inputs "no", then the game closes out with the message "Scram punk!"
        quit_or_play = get_yes_no('\nCare to play again? (Y/N): ')
    print('\nScram punk!')

main()
