import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):
  """Represents the sleeping state for the puppy."""
  
  def play(self, puppy):
    """Returns a string describing the puppy's reaction to playing when asleep."""
    return "The puppy is asleep. It doesn't want to play right now."

  
  def feed(self, puppy):
    """Changes the state of the puppy: Sleeping -> Eating
    Returns: A string describing the puppy's reaction to food when asleep."""
    puppy.change_state(state_eat.StateEat())
    return " The puppy wakes up and comes running to eat"
  