import random
import maze


class Minotaur:
  """Creates an object representative of the minotaur ("M") in the maze.
  Attributes:
    _row (int): The row coordinate associated with the minotaur's location.
    _col (int): The column coordinate associated with the minotaur's location.
    _dir (str): The direction in which the minotaur will move to get closer to the hero.
    _turns (int): Number of turns since minotaur has last sensed the location of the hero."""

  def __init__(self):
    """Randomizes the location of the Minotaur within the maze file."""

    maze_grid = maze.Maze()._maze
    empty_cells = [
      (row, col)
      for row, items_in_row in enumerate(maze_grid)
      for col, cell in enumerate(items_in_row)
      if cell == " "
    ]
    if not empty_cells:
      raise ValueError("Cannot place the minotaur: maze has no empty spaces.")

    self._row, self._col = random.choice(empty_cells)
    maze_grid[self._row][self._col] = "M"

    self._dir = ''
    self._turns = 0

    # Allows the minotaur to move once the game has begun
    self._get_search_dir() 

  
  def _get_search_dir(self):
    """Selects the direction in which the minotaur will move in order to reach the hero."""

    # Iterates through the rows and columns of the maze to search for the hero ("H")
    for hero_row in range(maze.Maze().__len__()):
      for hero_col in range(len(maze.Maze()._maze[hero_row])):
        if maze.Maze()._maze[hero_row][hero_col] == 'H':

          
          # The minotair senses that the hero is in a different row and that it cannot
            # move left/right due to being between two walls
          # Thus, the minotaur can move up/down the column
          # Prevents the minotaur from getting stuck
          if self._row != hero_row and (maze.Maze()._maze[self._row-1][self._col] != '*' or maze.Maze()._maze[self._row+1][self._col]!='f'):

          # Moves left or right based on the whether the index of the hero is > or < the Minotaur's
            if hero_row < self._row:
              self._dir = "U"
            elif hero_row > self._row:
              self._dir = "D"

          
          # The minotaur senses that the player is either to its left or right
          # Moves left or right based on the whether the index of the hero is > or < the Minotaur's
          elif self._col != hero_col:
            if hero_col < self._col:
              self._dir = "L"
            elif hero_col > self._col:
              self._dir = "R"
              
          else:
            pass
            
    self._turns = 0

  
  def move_minotaur(self):
    """Moves the minotaur in the direction given by the 'Search Direction' method."""

    # Updates the direction in which the minotaur should be moving in order to
      # get closer to the hero
    if self._turns == 3:
      self._get_search_dir()

    # Moves the minotaur up when the space above it is not a wall or the finish "f"
    # Otherwise, the minotaur cannot move up and remains still
    if self._dir == "U":
      if maze.Maze()._maze[self._row - 1][self._col] == '*' or maze.Maze()._maze[self._row - 1][self._col] == 'f':
        maze.Maze()._maze[self._row][self._col] = "M"
      else:
        maze.Maze()._maze[self._row][self._col] = " "
        prev_char = maze.Maze()._maze[self._row - 1][self._col]
        maze.Maze()._maze[self._row - 1][self._col] = "M"
        self._row -= 1
        return prev_char
        
    # Moves the minotaur down when the space above it is not a wall
    # Otherwise, the minotaur cannot move down and remains still
    elif self._dir == "D":
      if maze.Maze()._maze[self._row + 1][self._col] == '*' or maze.Maze()._maze[self._row - 1][self._col] == 'f':
        maze.Maze()._maze[self._row][self._col] = "M"
      else:
        maze.Maze()._maze[self._row][self._col] = " "
        prev_char = maze.Maze()._maze[self._row - 1][self._col]
        maze.Maze()._maze[self._row + 1][self._col] = "M"
        self._row += 1
        return prev_char

    # Moves the minotaur left when the space above it is not a wall
    # Otherwise, the minotaur cannot move left and remains still
    elif self._dir == "L":
      if maze.Maze()._maze[self._row][self._col - 1] == '*' or maze.Maze()._maze[self._row - 1][self._col] == 'f':
        maze.Maze()._maze[self._row][self._col] = "M"
      else:
        maze.Maze()._maze[self._row][self._col] = " "
        prev_char = maze.Maze()._maze[self._row][self._col - 1]
        maze.Maze()._maze[self._row][self._col - 1] = "M"
        self._col -= 1
        return prev_char

    # Moves the minotaur right when the space above it is not a wall
    # Otherwise, the minotaur cannot move right and remains still
    else:
      if maze.Maze()._maze[self._row][self._col + 1] == '*' or maze.Maze()._maze[self._row - 1][self._col] == 'f':
        maze.Maze()._maze[self._row][self._col] = "M"
      else:
        maze.Maze()._maze[self._row][self._col] = " "
        prev_char = maze.Maze()._maze[self._row][self._col + 1]
        maze.Maze()._maze[self._row][self._col + 1] = "M"
        self._col += 1
        return prev_char

    self._turns += 1
