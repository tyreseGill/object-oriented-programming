import monster

class Alien(monster.Monster):
    """An extension of the Monster class that represents an alien monster."""
  
    def __init__(self):
      """Initializes the name and HP of the monster through superclass."""
      super().__init__('Alien', 7)


    def attack(self):
      """Returns an integer represenative of the base attack power of the monster."""
      return 3