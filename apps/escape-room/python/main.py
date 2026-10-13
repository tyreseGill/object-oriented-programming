import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import random
import door, basic_door, deadbolt_door, locked_door


def open_door(door):
  """Gives a description, menu options, and clues associated with the given door object.
  Args:
    door (obj): A class object representative of type of door that the user is dealing with at the moment."""
  
  print()
  print(door.examine_door())
  
  door.attempt(get_int_range(door.menu_options(),1,door.get_menu_max()))

  # Checks whether the door is unlocked or if the user needs a clue
  if door.is_unlocked():
    print(door.success())
  else:
    print(door.clue())


def main():
  """Repeats the process of the user attempting to open a door until all three doors have been unlocked."""
  
  print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")

  # Adds three random types of door objects to a list
  doors = []
  for i in range(3):
    random_int = random.randint(1,3)
    if random_int == 1:
      doors.append(basic_door.BasicDoor())
    elif random_int == 2:
      doors.append(deadbolt_door.DeadboltDoor())
    else:
      doors.append(locked_door.LockedDoor())

  # User goes through process of unlocking and moving to the next door
    # Continues until all doors have been unlocked
  while len(doors) > 0:
    open_door(doors[0])
    if doors[0].is_unlocked():
      doors.remove(doors[0])
      
  print("\nCongratulations! You've escaped!")
    
main()