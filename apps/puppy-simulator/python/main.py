import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import puppy


def main():
  """Displays a menu and repeatedly prompts the user to either feed or play with their puppy until they decide to quit."""
  
  pup = puppy.Puppy()
  print("You have a new puppy! Congrats!\nWhat would you like to do with your puppy?")
  choice = get_int_range("1. Feed it\n2. Play with it\n3. Exit\nPick Your Choice: ", 1,3)

  while choice != 3:
    
    if choice == 1:
      # Food is given to puppy
      pup.inc_feeds()
      print(pup.give_food())
      
    else:
      # Puppy is played with
      pup.inc_plays()
      print(pup.throw_ball())
    
    choice = get_int_range("1. Feed it\n2. Play with it\n3. Exit\nPick Your Choice: ", 1,3)

  # Displayed when player chooses to exit simulation
  print("You have now left the simulation.")
  

main()