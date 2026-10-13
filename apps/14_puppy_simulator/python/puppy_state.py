import abc 

class PuppyState(abc.ABC):
  """Represents the interface for the states associated with a puppy."""

  @abc.abstractmethod
  def feed(self, puppy):
    """Serves as placeholder to be overridden when defining the puppy's reaction to food during a specific state."""
    pass

  
  @abc.abstractmethod
  def play(self, puppy):
    """Serves as placeholder to be overridden when defining the puppy's reaction to play during a specific state."""
    pass
