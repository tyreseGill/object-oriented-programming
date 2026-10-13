import monster

class Undead(monster.Monster):
  """An extension of the Monster class that represents an undead monster."""
  
  def __init__(self):
    """Initializes the name and HP of the monster through superclass."""
    super().__init__('Undead', 2)

  
  def attack(self):
    """Returns an integer represenative of the base attack power of the monster."""
    return 5