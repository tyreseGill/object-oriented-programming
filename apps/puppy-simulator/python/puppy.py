import state_asleep

class Puppy:
  """Represents a puppy object.
  Attributes:
    _states: 
    _feeds:
    _plays:
    """
  
  def __init__(self):
    """Represents the default attributes of the dog when in the sleeping state."""
    self._plays = 0
    self._feeds = 0
    self._state = state_asleep.StateAsleep()
    
  @property
  def plays(self):
    """Accesses the counter variable for playing."""
    return self._plays

  
  @property
  def feeds(self):
    """Accesses the counter variable for eating."""
    return self._feeds

  
  def change_state(self, new_state):
    """Changes the state of the puppy."""
    self._state = new_state

  
  def throw_ball(self):
    """Returns the play method for the puppy for whatever state it's in."""
    return self._state.play(self)

  
  def give_food(self):
    """Returns the feed method for the puppy for whatever state it's in."""
    return self._state.feed(self)

  
  def inc_feeds(self):
    """Increments the counter for eating."""
    self._feeds +=1 

  
  def inc_plays(self):
    """Increments the counter for playing."""
    self._plays += 1

  
  def reset(self):
    """Restores the counters associated with playing and sleeping for the dog after it wakes from sleep."""
    self.__init__()