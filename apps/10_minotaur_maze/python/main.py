import maze
import hero
import minotaur


def main():
  """Runs through loop constantly prompting the user to move a certain direction in the maze and have the minotaur move accordingly."""
  
  maze_puzzle = maze.Maze()
  player = hero.Hero()
  monster = minotaur.Minotaur()

  while True:
  
    output = ''
    mino_output = ''
    print(maze_puzzle)

    # prompts the user to enter a valid input regarding the direction of their movement
    user_dir = str(input("Choose a Direction (WASD): "))
    if user_dir.upper() != "W" and user_dir.upper() != "A" and user_dir.upper(
    ) != "S" and user_dir.upper() != "D":
      print("Please input either 'W', 'A', 'S', or 'D'.")
      while user_dir.upper() != "W" and user_dir.upper(
      ) != "A" and user_dir.upper() != "S" and user_dir.upper() != "D":
        user_dir = input("Choose a Direction (WASD): ")

    # Moves the hero in the direction specified 
    # Stores the item previously at the space where the hero moved
    if user_dir.upper() == "W":
      output = player.go_up()
    elif user_dir.upper() == "A":
      output = player.go_left()
    elif user_dir.upper() == "S":
      output = player.go_down()
    else:
      output = player.go_right()

    # Prints the corresponding statement based on the symbol located at the space the hero moved to
    if output == '*':
      print("You ran into a wall!")
    elif output == 'M':
      print("You ran into the minotaur, game over!")
      exit()
    elif output == 'f':
      print("Congratulations, you escaped the minotaur!")
      exit()

    # Moves the minotaur during each turn
    # Stores the item previously at the space where the minotaur moved
    # Checks if the minotaur is on the same space as the hero
    mino_output = monster.move_minotaur()
    if mino_output == 'H':
      print("The minotaur caught you! Game over!")
      exit()



main()
