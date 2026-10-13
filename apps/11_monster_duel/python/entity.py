import abc

class Entity(abc.ABC):
  
  def __init__(self, name, hp):
    self._name = name
    self._hp = hp
    
  @property
  def get_name(self): # remove get
    return self._name
    
  @property
  def get_hp(self): # remove get
    return self._hp
    
  def take_damage(self, dmg):
    self._hp -= dmg
    if self.get_hp < 0:
      self._hp = 0

  def is_alive(self):
    return self._hp > 0
      
  def __str__(self):
    return f"{self.get_name} HP: {self.get_hp}"
    
  @abc.abstractmethod
  def melee_attack(self, entity):
    pass