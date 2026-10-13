import door
import random


class LockedDoor(door.Door):
  """Represents a door that is locked and requires a key."""
  
  def __init__(self):
    """Randomizes the location of the key."""
    self._key_location = random.randint(1,3)
    self._input = None

    
  def examine_door(self):
    """Returns a string describing the door and the actions necessary to unlock it."""
    return "A locked door. Look around for the key."

    
  def menu_options(self):
    """Returns a string displaying the menu options related to the locked door."""
    return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock.\n"


  def get_menu_max(self):
    """Returns an integer representative of the number of options to choose from the menu for the locked door."""
    return 3

    
  def attempt(self, option):
    """Determines whether the user has unlocked the door based on the option chosen from the menu.
    Args:
      option (int): An integer representative of the user's choice regarding a course of action related to the door.
    Returns: A string describing the action chosen by the user."""

    # Checks if the location inspected by the user is where the key is
    if option == self._key_location:
      self._input = 0

    # Returns the corresponding string based on the user's input
    if option == 1:
      return "You look under the mat..."
    elif option == 2:
      return "You look under the flower pot..."
    else:
      return "You look under the fake rock..."

      
  def is_unlocked(self):
    """Determines whether the locked door has been unlocked."""
    if self._input == 0:
      return True
    else:
      return False

      
  def clue(self):
    """Returns a string prompting the user to check elsewhere for the key."""
    return "Look somewhere else."

    
  def success(self):
    """Returns a string signifying that the locked door has been unlocked."""
    if self.is_unlocked():
      return "Congratulations, you unlocked the door!\n"
      