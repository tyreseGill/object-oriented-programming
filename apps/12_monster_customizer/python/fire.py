import decorator

class Fire(decorator.Decorator):
  def __init__(self, monst):
    monst.name = 'Firey ' + monst.name
    monst.hp = monst.hp + 3
    super().__init__(monst)
  def attack(self):
    return super().attack() + 3