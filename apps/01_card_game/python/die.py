import random

class Die:
  '''Represents a single Die.  Defaults to a 6-sided die.
      Attributes:
        Sides (int): Number of sides on the die.
        Value (int): The value of the rolled die.'''

  def __init__(self, sides=6):
    '''Sets the number of sides of the die (default 6).'''
    self.sides = sides
    self.value = self.roll()

  def roll(self):
    '''Rolls the die to set the value of the die.  Returns that value (random
    value between 1-sides).'''
    self.value = random.randint(1, self.sides)
    return self.value

  def __eq__(self, other):
    '''Compares the two dice to see if self’s value is equal to the other’s value.'''
    return self.value == other.value

  def __lt__(self, other):
    '''Compares the two dice to see if self’s value is less than the other’s
    value.'''
    return self.value < other.value
  
  def __sub__(self, other):
    '''Returns the difference of the values of self and other'''
    return self.value - other.value

  def __str__(self):
    '''Returns the string representation of the die.'''
    return str(self.value)
    