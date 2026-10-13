import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import random


def weapon_menu():
    '''Asks the user to input one of four valid options from the weapon menu.'''

    user_choice = input('\nChoose your weapon: \nR. Rock\nP. Paper\nS. Scissors\nB. Back\n')

    if ((user_choice != 'R') and (user_choice != 'r')) and ((user_choice != 'P') and (user_choice != 'p')) and ((user_choice != 'S') and (user_choice != 's')) and ((user_choice != 'B') and (user_choice != 'b')):
        # If the user selects 'R', 'P', or 'S', the game will proceed to determine a winner between the user and the
        # computer. But if the user inputs 'B', the user will default back to the main menu.

        while ((user_choice != 'R') and (user_choice != 'r')) and ((user_choice != 'P') and (user_choice != 'p')) and ((user_choice != 'S') or (user_choice != 's')) and ((user_choice != 'B') and (user_choice != 'b')):
            print('\nTry again!')
            user_choice = input('\nChoose your weapon: \nR. Rock\nP. Paper\nS. Scissors\nB. Back\n')

    return user_choice


def comp_weapon():
    '''Randomly returns either Rock, Paper, or Scissors for the Computer.'''

    comp_options = ["R", "P", "S"]
    comp_choice = random.choice(comp_options)
    return comp_choice


def find_winner(player, comp):
    '''Compares the strings from the parameters,'player' and 'comp', to determine the winner and will return
    either a 0, 1, or 2 based on the outcome.'''

    if ((player == "R") or (player == "r")) and comp == "S":
        print("You crushed Computer's Scissors with your Rock!\nPlayer wins!")
        return 1

    elif ((player == "R") or (player == "r")) and comp == "P":
        print("You made the mistake of selecting Rock to Computer's Paper!\nComputer wins!")
        return 2

    elif ((player == "S") or (player == "s")) and comp == "R":
        print("Computer countered your Scissors with Rock!\nComputer wins!")
        return 2

    elif ((player == "S") or (player == "s")) and comp == "P":
        print("You cut Computer's Paper to ribbons with your Scissors!\nPlayer wins!")
        return 1

    elif ((player == "P") or (player == "p")) and comp == "R":
        print("You used Paper to envelop Computer's Rock!\nPlayer wins!")
        return 1

    elif ((player == "P") or (player == "p")) and comp == "S":
        print("Sorry, but Scissors beats Paper any time of the week!\nComputer wins!")
        return 2

    else:
        # When the Player and Computer both utilize the same weapon, a specific statement will be outputted and 0 is returned.

        if ((player == "R") or (player == "r")) and comp == "R":
            print("What's this?! It seems both you and Computer have chosen Rock!\nIt's a tie!")
        elif ((player == "P") or (player == "p")) and comp == "P":
            print("Both you and Computer chose Paper!\nIt's a draw!")
        elif ((player == "S") or (player == "s")) and comp == "S":
            print("Scissors can't beat another pair of Scissors!\nIt's a stalemate!")
        return 0


def display_scores(player_score, comp_score):
    '''Prints out the scores associated with the Player and Computer respectively.'''
    print("Player =", player_score, "\nComputer =", comp_score)


def main():
    '''A main function consisting of a while loop which refers to four smaller functions declared within itself.'''

    player_score, comp_score = 0, 0
    game = True

    while game:
        # Unless the user chooses to quit, the while loop will continue to ask them for input in the form of 1, 2, and 3
        # in order to continue playing the game.

        user_input = get_int_range("\nRPS Menu:\n1. Play game\n2. Show Score\n3. Quit\n", 1, 3)

        while user_input == 1:
            # When the user inputs 1, the program compares the items selected by the user and Computer to determine the winner.
            user = weapon_menu()

            if (user == "B") or (user == "b"):
                # Exits loop to go back to main menu.
                break

            # If the user doesn't want to go back to the main menu, the program proceeds to get the weapon used by the Computer.
            # and determine the winner
            comp = comp_weapon()
            winner = find_winner(user, comp)

            # Either increments the score of the Player, Computer, or neither depending on the value of 'winner'.
            if winner == 1:
                player_score += 1
            elif winner == 2:
                comp_score += 1
            else:
                None

        if user_input == 2:
            # When the user inputs 2, the program shows the scores of the Player and Computer respectively.
            display_scores(player_score, comp_score)

        elif user == "B" or user == "b":
            # Catches when user wants to Back to the Main Menu and proceeds to reset the value of user to None and
            # Goes back to the beginning of original loop to get Menu.
            user = None
            continue

        else:
            # When the user inputs the only other valid input (that being 3), the game will default to this statement
            # Assigns 'game' the value of 'False', thereby making the condition for the while loop false and ending the game.
            print("Final Score\nPlayer =", player_score, "\nComputer =", comp_score)
            game = False


main()
