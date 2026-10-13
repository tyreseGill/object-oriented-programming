import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import fire
import flying
import lasers
import poison
import alien
import beast
import undead


def main():
  """Asks the user to choose a base monster and add new abilities to said monster to their liking until the user chooses to quit."""

  # Prompts the user to choose one of three monsters to decorate as their base
  print("\nMonster Maker!")
  base_monster_chosen = get_int_range("\nChoose a base monster:\n1. Alien\n2. Beast\n3. Undead\nEnter choice: ", 1, 3)

  # Creates the base monster according to the number inputted by the user
  if base_monster_chosen == 1:
    monster = alien.Alien()
  elif base_monster_chosen == 2:
    monster = beast.Beast()
  else:
    monster = undead.Undead()

  # Repeatedly prompts the user to add new abilities to their monster until they quit
  while True:

    # Prints name, HP, and attack power of monster
    # Prompts user to add abilty to their monster or quit
    print()
    print(monster)
    ability = get_int_range("\nAdd an ability:\n1. Fire\n2. Flying\n3. Lasers\n4. Poison\n5. Quit\nEnter ability: ", 1, 5)

    # Decorates the base monster with the desired abilty selected by the user
    # Displays the final monster and exits program if user inputs "5"
    if ability == 1:
      monster = fire.Fire(monster)
    elif ability == 2:
      monster = flying.Flying(monster)
    elif ability == 3:
      monster = lasers.Lasers(monster)
    elif ability == 4:
      monster = poison.Poison(monster)
    else:
      print("\nYour final monster is...")
      print(monster)
      exit()
    

main()