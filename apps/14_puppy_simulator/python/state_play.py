import puppy_state
import random

class StatePlay(puppy_state.PuppyState):
  """Represents the playing state for the puppy."""
  
  def play(self, puppy):
    """Determines whether the puppy will fall asleep or continue playing."""
    
    go_to_sleep = random.randint(2,3)

    # Puppy defaults to sleep state from playing too much
    if puppy.plays >= go_to_sleep:
      puppy.reset()
      return "The puppy got so tired it went to sleep."

    # Puppy remains in the play state
    else:
      return "You throw the ball again and the puppy excitedly chases it."
    
  def feed(self, puppy):
    """Returns string stating that the dog is distracted from playing."""
    return "The puppy is too busy playing with the ball to eat right now."
  