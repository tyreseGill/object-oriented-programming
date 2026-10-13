import sys
from pathlib import Path

# Make the repository-level shared package available when running this file directly.
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

import beginner_factory, expert_factory, hero
from shared.check_input import get_int_range


def main():
    player = hero.Hero()

    print("Welcome to the Monster Factory!\nYou are a hero who must defeat a series of enemies in order to save the kingdom. You will face a series of random enemies, and you must defeat them all to win the game.\n")

    difficulty = get_int_range(
        "Choose your difficulty level:\n1. Beginner\n2. Expert\nEnter your choice (1 or 2): ", 1, 2)

    # Create the appropriate factory based on the chosen difficulty level
    if difficulty == 1:
        factory = beginner_factory.BeginnerFactory()
    else:
        factory = expert_factory.ExpertFactory()

    # Main game loop
    while player.is_alive():
        enemy = factory.create_random_enemy()
        print(f"\nA wild {enemy.get_name} has appeared! It has {enemy.get_hp} health points.")

        # Battle loop
        while enemy.is_alive() and player.is_alive():
            action = get_int_range("\nWhat would you like to do?\n1. Attack\n2. Heal\nEnter your choice (1 or 2): ", 1, 2)

            # Perform the chosen action
            if action == 1:
                print(player.melee_attack(enemy))
                if enemy.is_alive():
                    print(enemy.melee_attack(player))
            else:
                player.heal()
                print(f"You healed yourself for 10 health points. Your current health is {player.get_hp}.")

        if not player.is_alive():
            print("\nYou have been defeated! Game over.")
            break
        else:
            print(f"\nYou have defeated the {enemy.get_name}! Your current health is {player.get_hp}.")


if __name__ == "__main__":
    main()
