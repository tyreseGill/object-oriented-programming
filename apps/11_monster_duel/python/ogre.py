import entity
import random
class Ogre(entity.Entity):
  
  def __init__(self):
    """Initializes an entity with the characteristics of an expert Ogre."""
    super().__init__('Expert Ogre', random.randint(8, 12))
    
  def melee_attack(self, entity):
    dmg = random.randint(6, 10)
    entity.take_damage(dmg)
    return super().get_name + ' attacks ' + entity.get_name + ' for ' + str(dmg) + ' damage.'