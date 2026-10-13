import maze

class Hero:
  """Creates an object representative of the hero ("H") in the maze.
  Attributes:
    _row: The row coordinate associated with the hero's location.
    _col: The column coordinate associated with the hero's location."""

  def __init__(self):
    """Sets up the hero's ("H") coordinates to default to that of the starting point ("s")."""
    self._row = maze.Maze().find_start()[0]
    self._col = maze.Maze().find_start()[1]
    maze.Maze()._maze[self._row][self._col] = "H"

  
  def go_up(self):
    """Moves the hero up one space if said space is not a wall.
    Returns: The item previously located at the space where the hero moved."""

    # Moves the hero up one space if the space is not a wall
    # Otherwise, the hero can't move that direction and remains still
    if maze.Maze()._maze[self._row - 1][self._col] == '*':
      maze.Maze()._maze[self._row][self._col] = 'H'
      return '*'
    else:
      maze.Maze()._maze[self._row][self._col] = " "
      prev_char = maze.Maze()._maze[self._row - 1][self._col]
      maze.Maze()._maze[self._row - 1][self._col] = "H"
      self._row -= 1
      return prev_char

  
  def go_down(self):
    """Moves the hero down one space if said space is not a wall.
    Returns: The item previously located at the space where the hero moved."""

    # Moves the hero down one space if the space is not a wall
    # Otherwise, the hero can't move that direction and remains still
    if maze.Maze()._maze[self._row + 1][self._col] == '*':
      maze.Maze()._maze[self._row][self._col] = 'H'
      return '*'
    else:
      maze.Maze()._maze[self._row][self._col] = " "
      prev_char = maze.Maze()._maze[self._row + 1][self._col]
      maze.Maze()._maze[self._row + 1][self._col] = "H"
      self._row += 1
      return prev_char

  
  def go_left(self):
    """Moves the hero left one space if said space is not a wall.
    Returns: The item previously located at the space where the hero moved."""

    # Moves the hero left one space if the space is not a wall
    # Otherwise, the hero can't move that direction and remains still
    if maze.Maze()._maze[self._row][self._col - 1] == '*':
      maze.Maze()._maze[self._row][self._col] = 'H'
      return '*'
    else:
      maze.Maze()._maze[self._row][self._col] = " "
      prev_char = maze.Maze()._maze[self._row][self._col - 1]
      maze.Maze()._maze[self._row][self._col - 1] = "H"
      self._col -= 1
      return prev_char

  
  def go_right(self):
    """Moves the hero right one space if said space is not a wall.
    Returns: The item previously located at the space where the hero moved."""

    # Moves the hero right one space if the space is not a wall
    # Otherwise, the hero can't move that direction and remains still
    if maze.Maze()._maze[self._row][self._col + 1] == '*':
      maze.Maze()._maze[self._row][self._col] = 'H'
      return '*'
    else:
      maze.Maze()._maze[self._row][self._col] = " "
      prev_char = maze.Maze()._maze[self._row][self._col + 1]
      maze.Maze()._maze[self._row][self._col + 1] = "H"
      self._col += 1
      return prev_char