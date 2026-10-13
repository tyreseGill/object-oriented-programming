import entity
import random


class Troll(entity.Entity):
  """L"""
  
  def __init__(self):
    """Initializes an entity with the characteristics of an expert Troll."""
    super().__init__('Expert Troll', random.randint(6, 10))
    
  def melee_attack(self, entity):
    dmg = random.randint(5, 8)
    entity.take_damage(dmg)
    return super().get_name + ' attacks ' + entity.get_name + ' for ' + str(dmg) + ' damage.'