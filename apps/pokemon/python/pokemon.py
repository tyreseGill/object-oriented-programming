import abc
import random


class Pokemon(abc.ABC):
  """A represents a pokemon.
  Attributes:
    name (str): The name of the specified pokemon.
    type (int): Used to indicate that a move is either normal or special."""

  
  def __init__(self, name, type):
    """Initializes the attributes for our pokemon object.
    Args:
      name (str): The name of the specified pokemon.
      type (int): Used to indicate that a move is either normal or special."""
    self._battle_table = [[1, 0.5, 2], [2, 1, 0.5], [0.5, 2, 1]] 
    self._name = name
    self._hp = 25                                               
    self._type = type

  
  def get_hp(self):
    """Returns the number of health points of the pokemon."""
    return self._hp

  
  def get_normal_menu(self):
    """Returns a string represenative of the normal menu."""
    return "Choose a Move:\n1. Slam\n2. Tackle\nEnter move: "

  
  def _normal_move(self, opponent, move):
    """Determines whether the move chosen calls for a slam or tackle attack.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
      move (int): An integer representative of the type of normal move that the pokemon will carry out.
    Returns: A function call to the corresponding attack."""
    if move == 1:
      return self._slam(opponent)
    else:
      return self._tackle(opponent)

  
  def _slam(self, opponent):
    """Performs the slamming attack on the opposing pokemon.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
    Returns: A string indicating the attack, its damage, and to whom it was dealt."""
    dmg = random.randint(1, 8)
    opponent._take_damage(dmg)
    return self._name + " SLAMS " + opponent._name + " for " + str(dmg) + " damage."

  
  def _tackle(self, opponent):
    """Performs the tackling attack against the opposing pokemon.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
    Returns: A string indicating the attack, its damage, and to whom it was dealt."""
    dmg = random.randint(3, 6)
    opponent._take_damage(dmg)
    return self._name + " TACKLES " + opponent._name + " for " + str(dmg) + " damage."

  
  @abc.abstractmethod
  def get_special_menu(self):
    """Retrieves the special attack menu for the Pokemon."""
    pass

  
  @abc.abstractmethod
  def _special_move(self, opponent, move):
    """Performs the special move specified for the Pokemon.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
      move (int): An integer representative of the type of normal move that the pokemon will carry out."""
    pass

  
  def attack(self, opponent, type, move):
    """Determines whether the attack move against the opposing pokemon will be normal or special.
    Args:
      opponent (object): An class object representative of the Gym Leader's pokemon the player is currently fighting.
      type (int): An integer used to indicate that a move is either normal or special.
      move (int): An integer representative of the type of normal move that the pokemon will carry out.
    Returns: A string indicating the attack, its damage, and to whom it was dealt."""
    if type == 1:
      return self._normal_move(opponent, move)
    else:
      return self._special_move(opponent, move)

  
  def __str__(self):
    """Returns a string displaying the name of the pokemon and it's HP."""
    return self._name + ": " + str(self._hp) + "/25"

  
  def _take_damage(self, dmg):
    """Lowers the HP of the pokemon based on the damage inflicted.
    Args:
      dmg (int): The amount of HP to be deducted."""
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0
