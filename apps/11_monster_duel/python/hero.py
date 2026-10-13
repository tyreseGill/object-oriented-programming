import entity
import random

class Hero(entity.Entity):
  
  def __init__(self, name="Hero"):
    """Initializes an entity with the characteristics of the hero."""
    super().__init__(name, 25)

  def heal(self):
    self._hp += 10
    
  def melee_attack(self, entity):
    
    dmg = random.randint(2, 6)
    entity.take_damage(dmg)
    return super().get_name + ' slashes a ' + entity.get_name + ' with a sword for ' + str(dmg) + ' damage.'
  
  def ranged_attack(self, entity):
    dmg = random.randint(1, 12)
    entity.take_damage(dmg)
    return super().get_name + ' rains a shower of arrows on ' + entity.get_name + ' for ' + str(dmg) + ' damage.'