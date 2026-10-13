import die

class Player:
  """Represents a single player in a game of Yahtzee.
  Attributes:
    dice (int): A list of three Die objects.
    player_points (int): The number of points achieved by the player."""
  
  def __init__(self):
    """Creates a list consisting of three objects representative of dice and sets the player's points to a default value of 0."""
    self.dice = [die.Die(), die.Die(), die.Die()]
    self.player_points = 0
    
  def get_points(self):
    """Returns the number of points obtained by the player."""
    return self.player_points

  def has_pair(self):
    """Compares the equality of the three dice to see if there exists a pair among them such that
    two dice are equivalent. Increments player_points by 1 and returns 'True' if the conditions are met."""
    if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2] or self.dice[0] == self.dice[2]:
      self.player_points += 1
      return True
    
  def has_three_of_a_kind(self):
    """Compares the equality of the three dice to see if they are all equivalent. Increments player_points by 3 and returns 'True' if the conditions are met."""
    if self.dice[2].__eq__(self.dice[1]) and self.dice[1].__eq__(self.dice[0]):
      self.player_points += 3
      return True
    
  def has_series(self):
    """Compares the difference between the dice to see if they form a series. Increments player_points by 2 and returns 'True' if the conditions are met."""
    if self.dice[2].__sub__(self.dice[1]) == 1 and self.dice[1].__sub__(self.dice[0]) == 1:
      self.player_points += 2
      return True

  def roll_dice(self):
    """Rolls each Die object and sorts the list for the dice"""

    # Rolls each die from the list and assigns each a value
    for d in self.dice:
      d.roll()

    # Sorts the list of dice in order from least to greatest
    for i in range(len(self.dice) - 1):
      for j in range(i + 1, len(self.dice)):
        if self.dice[j].__lt__(self.dice[i]):
          temp = self.dice[i]
          self.dice[i] = self.dice[j]
          self.dice[j] = temp
    
  def __str__(self):
    """Returns a string displaying the values of each die and the corresponding statement alond with the user's score"""

    # Sorts the dice and concatenates a string to display the values of each die
    string = ""
    self.dice.sort()
    for i, d in enumerate(self.dice):
      string += "D" + str(i + 1) + "= " + str(d) + " "

    string += "\nScore = " + str(self.player_points)
    return string
    