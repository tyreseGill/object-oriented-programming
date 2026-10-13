import decorator

class Flying(decorator.Decorator):
  """An extension of the Decorator class that represents the ability for flying."""
  
  def __init__(self, monst):
    """Updates the name and health of the monster gaining the ability."""
    monst.name = 'Flying ' + monst.name
    monst.hp = monst.hp + 2
    super().__init__(monst)

  
  def attack(self):
    """Increases the attack power of the monster with the additional ability."""
    return super().attack() + 4