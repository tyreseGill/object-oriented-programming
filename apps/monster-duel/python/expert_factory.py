import enemy_factory
import random
import troll
import ogre
import goblin

class ExpertFactory(enemy_factory.EnemyFactory):
  """An extension of EnemyFactory which serves to create difficult enemies."""
  
  def create_random_enemy(self):
    """"""
    enemy_list = ["Troll", "Ogre", "Goblin"]
    random_enemy = random.choice(enemy_list)
    
    if random_enemy == "Troll":
      return troll.Troll()
    elif random_enemy == "Ogre":
      return ogre.Ogre()
    else:
      return goblin.Goblin()