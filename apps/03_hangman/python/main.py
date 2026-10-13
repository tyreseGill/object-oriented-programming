import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_yes_no

import random
import dictionary


def display_gallows(num_incorrect):
    '''Repeatedly compares the value of num_incorrect to determine the state of the gallows based on the number of
    incorrect inputs provided by the user
    Args:
        num_incorrect: The number of times the user has inputted an incorrect letter for a given word from the
        dictionary
    Returns:
        A series of print statements which portray the gallows for 'Hangman'
        The higher the value associated with num_incorrect, the more developed the gallows to be printed
    '''

    if num_incorrect == 0:
        print("\n========")
        print("||/   |")
        print("||")
        print("||")
        print("||")
        print("||")
    elif num_incorrect == 1:
        print("\n========")
        print("||/   |")
        print("||    O")
        print("||")
        print("||")
        print("||")
    elif num_incorrect == 2:
        print("\n========")
        print("||/   |")
        print("||    O")
        print("||    |")
        print("||")
        print("||")
    elif num_incorrect == 3:
        print("\n========")
        print("||/   |")
        print("||    O")
        print("||    |")
        print("||   /")
        print("||")
    elif num_incorrect == 4:
        print("\n========")
        print("||/   |")
        print("||    O")
        print("||    |")
        print("||   / \\")
        print("||")
    elif num_incorrect == 5:
        print("\n========")
        print("||/   |")
        print("||  \\ O")
        print("||    |")
        print("||   / \\")
        print("||")
    elif num_incorrect == 6:
        print("\n========")
        print("||/   |")
        print("||  \\ O /")
        print("||    |")
        print("||   / \\")
        print("||")


def display_correct(correct):
    '''Updates the display associated with correct letters guessed by the user
    Args:
        Correct: A list made up of the correct letters inputted by the user
    Returns:
        A print statement that displays the correct letters guessed by the user separated by spaces
    '''
    print('Correct:', *correct)


def display_incorrect(incorrect):
    '''Updates the display associated with incorrect letters guessed by the user
    Args:
        Incorrect: A list made up of the incorrect letters inputted by the user
    Returns:
        A print statement that displays the incorrect letters guessed by the user separated by spaces
    '''
    print("\nIncorrect Selections:", *incorrect)


def display_letters_remaining(incorrect, correct):
    '''Updates the list of letters not yet inputted by the user
    Args:
        Incorrect: A list made up of the incorrect letters inputted by the user
        Correct: A list made up of the correct letters inputted by the user
    Returns:
        A print statement that displays the letters that have not been inputted by the user yet
    '''

    # Separates a string of the alphabet into a list and creates a combined list for incorrect and correct gueses
    s = " "
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    used_letters = incorrect + correct

    for letters in used_letters:
        # Ensures that any letters in the list for incorrect and correct guesses are properly removed from the alphabetical
        # list of unused letters
        for letters in alphabet:
            if letters in incorrect:
                alphabet.remove(letters)
        for letters in alphabet:
            if letters in correct:
                alphabet.remove(letters)
    print("Letters remaining:", s.join(alphabet))


def main():
    '''Sets up the necessary variables and refers to more basic functions in order to simulate a round of 'Hangman'
        Returns:
            A simulated round of 'Hangman' which will persist until the user indicates that they want to quit
        '''

    # Sets up the proper variables necessary for the while loop and the proper running of "Hangman"
    print("\n-Hangman-")
    game = True
    word = dictionary.words[random.randint(0, len(dictionary.words) - 1)]
    correct = ['_', '_', '_', '_', '_']
    incorrect = []
    num_correct = 0
    num_incorrect = 0

    while game != False:
        # Until the user inputs "No" at the end of the loop, variable for the game variable will remain true and reset
        # to simulate another round
        guess = input("Enter a letter: ").upper()
        while guess.isalpha() == False:
            # If the user's input is not part of the alphabet, the user will be repeatedly prompted to enter a valid
            # letter until the statement is proven "True"
            print("\nSorry, but your input isn't valid. Please type a letter ranging from A-Z.")
            guess = input("\nEnter a letter: ").upper()

        if guess in (correct + incorrect):
            # When the user inputs a letter that they've already previous inputted, they will return to the beginning
            # of the loop where they will once again be prompted to enter a valid input
            print('You already entered that letter.')
            continue

        if guess in word:
            # True when the user inputs a letter that exists in the word
            # Compares the letter guessed to each individual character of our 5-letter word and overwrites the blank
            # spaces in the list for "correct" in the proper location based on the index of word
            print('You correctly guessed one of the letters!')
            for i in range(5):
                if guess == word[i]:
                    correct[i] = guess
                    num_correct += 1

        else:
            # When the user inputs a letter doesn't satisfy the previous two conditions, the letter inputted can only be
            # be assumed to not exist as part of the word
            # In response, the program increments the counter for incorrect guesses and adds it to the list for
            # incorrect guesses
            print("That letter wasn't a part of the word.")
            num_incorrect += 1
            if guess not in incorrect:
                incorrect.append(guess)
                incorrect.sort()

        # Calls the previously defined functions in order to output the necessary print statements based on correct and
        # incorrect guesses (counter as well) made by the user
        display_incorrect(incorrect)
        display_gallows(num_incorrect)
        display_correct(correct)
        display_letters_remaining(incorrect, correct)
        if num_correct == 5 or num_incorrect == 6:
            # Runs when the user has incremented the counters associated with the number of correct/incorrect guesses to the
            # point that the program recognizes that they've either won or lost the game

            if num_correct == 5:
                print("\nYou win!")
            elif num_incorrect == 6:
                print("\nYou lose! The answer was:", word + '!')

            game = get_yes_no('Try again? (Y/N): ')
            if game == False:
                exit()
            elif game == True:
                # If the user inputs "Yes", then the variable for game will prove "True" and the game reset
                main()


main()