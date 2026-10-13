import check_input
import random
import hero, hero_minotaur
from maze import Maze


def read_maze():
  maze = Maze()
  print(maze)

def find_start(maze):
  pass


# def display_maze(maze, loc):
#   """Displays the maze with the hero's location marked by an 'H'."""
#   for row in range(len(maze)):
#     for col in range(len(maze[row])):
#       if row == loc[0] and col == loc[1]:
#         print("H", end="")
#       else:
#         print(maze[row][col], end="")
#     print()


def main():
  print("-Maze Solver-")
  
  while True:
    print("\n1. Read Maze\n2. Display Maze\n3. Exit")
    choice = check_input.get_int_range("Enter your choice: ", 1, 3)
    
    if choice == 1:
      read_maze()
    elif choice == 2:
      maze_solver.display_maze(maze_solver.Maze()._maze, maze_solver.Maze().find_start())
    elif choice == 3:
      print("Exiting...")
      break

main()