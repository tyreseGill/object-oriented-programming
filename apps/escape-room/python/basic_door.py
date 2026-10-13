import door
import random

class BasicDoor(door.Door):
  """Represents a basic door."""
  
  def __init__(self):
    """Randomizes the initial state of the basic door."""
    self._state = random.randint(1,2)
    self._input = None

    
  def examine_door(self):
    """Returns a string describing the door and the actions necessary to unlock it."""
    return "You encounter a basic door, you can either push it or pull it to open"

    
  def menu_options(self):
    """Returns a string displaying the menu options related to the basic door."""
    return "1. Push\n2. Pull\n"

    
  def get_menu_max(self):
    """Returns an integer representative of the number of options to choose from the menu for the basic door."""
    return 2

    
  def attempt(self, option):
    """Determines whether the user has opened the door based on the option chosen from the menu.
    Args:
      option (int): An integer representative of the user's choice regarding a course of action related to the door.
    Returns: A string describing the action chosen by the user."""  

    # Checks if the directionality in which the door is opened and is supposed to open are the same
    if option == self._state:
      self._input = 0

    # Returns the corresponding string based on the user's input
    if option == 1:
      return "You push the door"
    else:
      return "You pull the door"

      
  def is_unlocked(self):
    """Determines whether the basic door has been opened."""
    if self._input == 0:
      return True
    else:
      return False

      
  def clue(self):
    """Returns a string indicating that the door opens in the opposite direction."""
    return "Try the other way."

    
  def success(self):
    """Returns a string signifying that the basic door has been unlocked."""
    if self.is_unlocked():
      return "Congratulations, you opened the door"
      