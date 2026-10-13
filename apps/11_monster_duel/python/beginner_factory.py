import enemy_factory
import random
import easy_goblin
import easy_ogre
import easy_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
  """An extension of EnemyFactory which serves to create easy enemies."""
  
  def create_random_enemy(self):
    """Randomly constructs an easy enemy (either a Troll, Ogre, Goblin)."""
    
    enemy_list = ["Troll", "Ogre", "Goblin"]
    random_enemy = random.choice(enemy_list)
    
    if random_enemy == "Troll":
      return easy_troll.EasyTroll()
    elif random_enemy == "Ogre":
      return easy_ogre.EasyOgre()
    else:
      return easy_goblin.EasyGoblin()