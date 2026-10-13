import decorator

class Poison(decorator.Decorator):
  """An extension of the Decorator class that represents the ability for flying."""
  
  def __init__(self, monst):
    monst.name = 'Poisonous ' + monst.name
    monst.hp = monst.hp + 4
    super().__init__(monst)
  def attack(self):
    return super().attack() + 2