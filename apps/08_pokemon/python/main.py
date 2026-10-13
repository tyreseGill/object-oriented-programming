import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from shared.check_input import get_int_range

import random
import fire
import grass
import water


def main():
  """Prompts the user to repeatedly attack the opponent until a winner has been decided."""
  
  gym_leader_pkmn = []
  opponent_type = random.randint(1, 3)

  # list of fire, water, and grass type pokemon names
  fire_type_names = [
    "Charmander", "Charmeleon", "Charizard", "Vulpix", "Ninetales",
    "Growlithe", "Arcanine", "Ponyta", "Rapidash", "Magmar", "Flareon",
    "Moltres"
  ]
  water_type_names = [
    "Squirtle", "Wartortle", "Blastoise", "Psyduck", "Golduck", "Poliwag",
    "Poliwhirl", "Poliwrath", "Tentacool", "Tentacruel", "Slowpoke", "Slowbro",
    "Seel", "Dewgong", "Shellder", "Cloyster", "Krabby", "Kingler", "Horsea",
    "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Magikarp",
    "Gyarados", "Lapras", "Vaporeon", "Omanyte", "Omastar", "Kabuto",
    "Kabutops"
  ]
  grass_type_names = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Oddish", "Gloom", "Vileplume",
    "Paras", "Parasect", "Bellsprout", "Weepinbell", "Victreebel", "Exeggcute",
    "Exeggutor", "Tangela"
  ]

  # Randomly selects three pokemon names based on the pokemon type assigned for the opponent
  if opponent_type == 1:
    for i in range(3):
      random_index = random.randint(0, 11)
      fire_pokemon_name = fire_type_names[random_index]
      gym_leader_pkmn.append(fire.Fire(fire_pokemon_name))
  elif opponent_type == 2:
    for i in range(3):
      random_index = random.randint(0, 31)
      water_pokemon_name = water_type_names[random_index]
      gym_leader_pkmn.append(water.Water(water_pokemon_name))
  else:
    for i in range(3):                                               
      random_index = random.randint(0, 13)
      grass_pokemon_name = grass_type_names[random_index]
      gym_leader_pkmn.append(grass.Grass(grass_pokemon_name))

  gym_pkmon_current = random.choice(gym_leader_pkmn)
  pokemon_type = get_int_range("Select the pokemon that you will fight with.\n1. I choose you, Charmander.\n2. Squirtle! GO!\n3. We can do it, Bulbasaur!\nChoose a Pokemon (1-3): ", 1, 3)
  player_pkmn = None

  # Assigns user the pokemon object of their choice
  if pokemon_type == 1:
    player_pkmn = fire.Fire("Charizard")
  elif pokemon_type == 2:
    player_pkmn = water.Water("Squirtle")
  else:
    player_pkmn = grass.Grass("Bulbasaur")

  print("\nLet the battle commence!")

  # Runs while loop to repeat the action of attacking the opponent until player wins or loses
  while True:
    
    print("GYM LEADER: I choose you\n" + str(gym_pkmon_current) + "\n")
    print(player_pkmn)

    # Pulls up the attack menu and asks for input
    attk_type_player = get_int_range(
      "Choose an Attack Type:\n1. Normal\n2. Special\nEnter attack type: ", 1,
      2)

    # Pulls up either the normal or special menu based on input
    if attk_type_player == 1: #attacking stuff for player
      player_nrml_move = get_int_range("\n" + player_pkmn.get_normal_menu(), 1, 2)
      print("\n" + player_pkmn.attack(gym_pkmon_current, 1, player_nrml_move)) 
    else:
      player_spcl_move = get_int_range("\n" + player_pkmn.get_special_menu(), 1, 2)
      print("\n" + player_pkmn.attack(gym_pkmon_current, 2, player_spcl_move))

    # Randomly selects the attack used by the Gym Leader
    attk_type_gym = random.randint(1,2)
    if attk_type_gym == 1:
      print(gym_pkmon_current.attack(player_pkmn, 1, random.randint(1,2))+"\n")
    else:
      print(gym_pkmon_current.attack(player_pkmn, 2, random.randint(1,2))+"\n")

    # Determines the winner based on health points and the number of pokemon left by Gym Leader
      # Breaks the loop when either the player has lost or won
    if player_pkmn.get_hp() == 0: 
      print("YOU LOSE")
      break
    elif gym_pkmon_current.get_hp() == 0:
      print("GYM LEADER: NOOOOO! You defeated my pokemon! ")
      if len(gym_leader_pkmn) == 1:
        print("YOU WON! You defeated the gym leader.")
        break
      else:
        gym_leader_pkmn.remove(gym_pkmon_current)
        gym_pkmon_current = random.choice(gym_leader_pkmn)
  
main()
