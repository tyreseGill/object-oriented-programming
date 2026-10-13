import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_yes_no

import player


def take_turn(player):
  """Rolls and displays the player's dice along with any win and updating the score."""

  player.roll_dice()
  player.get_points()
  
    # Checks the values of the dice rolled to determine whether the user got a series, three of a kind
    # a pair, or no special case at all.
  if player.has_series() == True:
    print("\nYou got a series!")
  elif player.has_three_of_a_kind() == True:
    print("\nYou got three of a kind!")
  elif player.has_pair() == True:
    print("\nYou got a pair!")
  else:
    print("\nToo bad, so sad!")

  print(player.__str__())


def main():
  """Sets up the object for a player playing Yahtzee. Runs until the player chooses to input 'No' and exits the program."""
  
  print("-Yahtzee-")
  player1 = player.Player()
  while True:
    take_turn(player1)
    boolean = get_yes_no("Play again? (Y/N): ")
    if boolean == False:
      print("\nGame Over")
      print("Final Score = " + str(player1.get_points()))
      exit()

main()