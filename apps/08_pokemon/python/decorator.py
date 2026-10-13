import monster

class Decorator(monster.Monster):
  def __init__(self, monst):
    super().__init__(monst.name, monst.hp)# pass in name and hp
    # set monster attribute to monster
    self._monster = monst
  def attack(self):
    return self._monster.attack()
  
