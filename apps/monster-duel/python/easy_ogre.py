import entity
import random

class EasyOgre(entity.Entity):
  
  def __init__(self):
    """Initializes an entity with the characteristics of an easy Ogre."""
    super().__init__("Ogre", random.randint(7,8))

  
  def melee_attack(self, entity):
    """Randomizes the attack damage dealt against another entity.
    Returns: A string describing the attack."""
    
    dmg = random.randint(5,8)
    entity.take_damage(dmg)
    return super().get_name + ' attacks ' + entity.get_name + ' for ' + str(dmg) + ' damage.'