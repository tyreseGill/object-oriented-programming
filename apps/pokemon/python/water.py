import random
import pokemon


class Water(pokemon.Pokemon):
  """Represents a water-type pokemon."""

  def __init__(self, name):
    """Inherits the attributes of the 'Pokemon' class and passes the corresponding name and type associated with a water-type pokemon."""
    super().__init__(name, 1)


  def get_special_menu(self):
    """Returns the special menu associated with a water-type pokemon."""
    return "Choose a Move:\n1. Water Gun\n2. Bubble Beam\nEnter move: "

  
  def _special_move(self, opponent, move):
    """Determines which of the two special moves listed in the special menu will be used against an opponent.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
      move (int): An integer representative of the type of normal move that the pokemon will carry out.
    Returns: The function call for the corresponding special move."""
    if move == 1:
      return self._water_gun(opponent)
    else:
      return self._bubble_beam(opponent)

  
  def _water_gun(self, opponent):
    """Performs the special water-type attack known as "Water Gun" on the opponent.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently.
    Returns: A string indicating the attack, its damage, and to whom it was dealt."""
    
    dmg = random.randint(1, 5)
    addon = ""

    # Applies damage multipliers based on the classification type of their opponent
    dmg *= self._battle_table[self._type][opponent._type]
    if opponent._type == 0:
      addon = "It was SUPER effective."
    elif opponent._type == 1:
      pass
    else:
      addon = "It was not very effective."

    # Applies the damage dealt to the opponent
    opponent._take_damage(int(dmg))
    
    return self._name + " squirts " + opponent._name + " with BUBBLE BEAM for " + str(
      int(dmg)) + " damage.\n" + addon

  
  def _bubble_beam(self, opponent):
    """Performs the special water-type attack known as "Bubble Beam" on the opponent.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently.
    Returns: A string indicating the attack, its damage, and to whom it was dealt."""
    
    dmg = random.randint(3, 4)
    addon = ""

    # Applies damage multipliers based on the classification type of their opponent
    dmg *= self._battle_table[self._type][opponent._type]
    if opponent._type == 0:
      addon = "It was SUPER effective."
    elif opponent._type == 1:
      pass
    else:
      addon = "It was not very effective."
    
    # Applies the damage dealt to the opponent
    opponent._take_damage(int(dmg))
    
    return self._name + " blasted " + opponent._name + " by using BUBBLE BEAM for " + str(
      int(dmg)) + " damage.\n" + addon
