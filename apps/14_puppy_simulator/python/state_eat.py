import puppy_state
import state_play
import random

class StateEat(puppy_state.PuppyState):
  """Represents the feeding state for the puppy."""

  
  def play(self, puppy):
    """Changes the state of the puppy: Eating -> Playing.
    Returns: A string describing the puppy's reaction to playing when eating."""
    puppy.change_state(state_play.StatePlay())
    return "The puppy looks up from its food and chases the ball you threw."

  
  def feed(self, puppy):
    """Determines whether the puppy will eat more food or fall asleep.
    Returns: A string describing the puppy's reaction to more food."""

    go_to_sleep = random.randint(2,3)

    # Puppy defaults to sleeping state in response to eating too much
    if puppy.feeds >= go_to_sleep:
      puppy.reset()
      return "The puppy ate so much it fell asleep!"

    # Puppy remains in the feeding state
    else:
      return "The puppy continues to eat as you add another schoop of kibble to its bowl"
    