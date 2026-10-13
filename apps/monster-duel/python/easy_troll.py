import entity
import random

class EasyTroll(entity.Entity):
  """An extension of the entity class. Represents the troll monster genereated by BeginnerFactory."""

  def __init__(self):
    """Initializes an entity with the characteristics of an easy Troll."""
    super().__init__("Troll", random.randint(5,7))

  
  def melee_attack(self, entity):
    """Randomizes the attack damage dealt against another entity.
    Returns: A string describing the attack."""
    
    dmg = random.randint(4,6)
    entity.take_damage(dmg)
    return super().get_name + ' attacks ' + entity.get_name + ' for ' + str(dmg) + ' damage.'