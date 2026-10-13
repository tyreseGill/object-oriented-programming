import monster

class Beast(monster.Monster):
  """An extension of the Monster class that represents a beast monster."""
  
  def __init__(self):
    """Initializes the name and HP of the monster through superclass."""
    super().__init__('Beast', 10)

  
  def attack(self):
    """Returns an integer represenative of the base attack power of the monster."""
    return 2