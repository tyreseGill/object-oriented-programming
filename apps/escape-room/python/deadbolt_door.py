import door
import random

class DeadboltDoor(door.Door):
  """Represents a deadbolted door."""
  
  def __init__(self):
    """Randomizes the state of the two deadbolts to the door."""
    self._bolt1 = random.randint(0,1)
    self._bolt2 = random.randint(0,1)

    
  def examine_door(self):
    """Returns a string describing the door and the actions necessary to unlock it."""
    return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they’re locked or unlocked."
    
  def menu_options(self):
    """Returns a string displaying the menu options related to the deadbolted door."""
    return "1. Toggle bolt 1\n2. Toggle bolt 2\n"
    
  def get_menu_max(self):
    """Returns an integer representative of the number of options to choose from the menu for the deadbolted door."""
    return 2
    
  def attempt(self, option):
    """Determines whether the user has unlocked the door based on the option chosen from the menu.
    Args:
      option (int): An integer representative of the user's choice regarding a course of action related to the door.
    Returns: A string describing the action chosen by the user."""

    # Switches the state of the specified deadbolt
    if option == 1:
      if self._bolt1 == 0:
        self._bolt1 = 1
      else:
        self._bolt1 = 0
    elif option == 2:
      if self._bolt2 == 0:
        self._bolt2 = 1
      else:
        self._bolt2 = 0

    # Returns the corresponding string based on the user's input
    if option == 1:
      return "You toggle the first bolt..."
    elif option == 2:
      return "You toggle the second bolt..."

  
  def is_unlocked(self):
    """Determines whether the deadbolted door has been unlocked."""
    if self._bolt1 == 0 and self._bolt2 == 0:
      return True
    else:
      return False

  
  def clue(self):
    """Returns a string indicating that either the door is partially or completely locked."""
    if self._bolt1 == 1 and self._bolt2 == 1:
      return "... it seems like it’s completely locked."
    else:
      return "You jiggle the door...it seems like one of the bolts is unlocked."

    
  def success(self):
    """Returns a string signifying that the deadbolted door has been unlocked."""
    if self.is_unlocked():
      return "Congratulations, you opened the door"
      