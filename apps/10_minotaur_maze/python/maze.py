import random

class Maze:
  """Creates a singleton object representative of the Minotaur's maze."""

  # Default values assigned when the Maze object is first created
  _instance = None
  _initialized = False

  
  def __new__(Maze):
    """Constructs, stores, and returns the class instance if the maze object hasn't beeen constructed yet. Else, the instance of the maze is returned in order to ensure that no more than one instance can exist.
    Args:
      Maze: An instance class variable.
    Returns: An instance of the class."""
    
    if Maze._instance is None:
      Maze._instance = super().__new__(Maze)
    return Maze._instance

  
  def __init__(self):
    """Creates and fills the 2D list based on the provided text file."""

    # Runs when the Maze object is initially created
    if not Maze._initialized:
      selected_maze = random.choice(["../txt/maze_1.txt", "../txt/maze_2.txt"])
      maze = open(selected_maze)
      maze_list = maze.readlines()

      # Iterates through each row and column within the maze
      # Stores the maze as a list of rows and their respective items
      # Sets initialized to 'True' to prevent the development of other Maze objects
      for i in range(len(maze_list)):
        row_elements = []
        for j in range(len(maze_list[i]) - 1):
          row_elements.append(maze_list[i][j])
        maze_list[i] = row_elements
      self._maze = maze_list
      Maze._initialized = True

  
  def __getitem__(self, row):
    """Returns a list containing all the items associated with the given row.
    Args:
      row (int): Represents the specified row from the maze file."""
    return self._maze[row]

  
  def __len__(self):
    """Returns the number of rows in the maze.
    Returns:
      num_rows (int): The number of rows present in the maze file."""
    num_rows = len(self._maze)
    return num_rows

  
  def __str__(self):
    """Returns the maze as a string and in a grid-format."""
    
    displayMaze = ''
    for i in range(len(self._maze)):
      for j in range(len(self._maze[i])):
        displayMaze += self._maze[i][j]
      displayMaze += '\n'
    return displayMaze

  
  def find_start(self):
    """Returns the location of the start ('S') symbol as a two-item list."""
    
    start = []
    for i in range(self.__len__()):
      for j in range(len(self._maze[i])):
        if self._maze[i][j] == 's':
          start.append(i)
          start.append(j)
    return start
