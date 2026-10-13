import decorator

class Lasers(decorator.Decorator):
  """An extension of the Decorator class that represents the ability for shooting lasers."""
  
  def __init__(self, monst):
    """Updates the name and health of the monster gaining the ability."""
    monst.name = monst.name + ' with Lasers'
    monst.hp = monst.hp + 1
    super().__init__(monst)

  
  def attack(self):
    """Increases the attack power of the monster with the additional ability."""
    return super().attack() + 5