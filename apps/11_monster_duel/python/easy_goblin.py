import entity
import random

class EasyGoblin(entity.Entity):
  
  def __init__(self):
    """Initializes an entity with the characteristics of an easy Goblin."""
    super().__init__("Goblin", random.randint(6,9))

  
  def melee_attack(self, entity):
    """Randomizes the attack damage dealt against another entity.
    Returns: A string describing the attack."""
    
    dmg = random.randint(5,9)
    entity.take_damage(dmg)
    return super().get_name + ' attacks ' + entity.get_name + ' for ' + str(dmg) + ' damage.'