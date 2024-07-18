import random
from game_slow_functions import *
from game_characters import *


def random_enemy(area):
    """
    A function to select a random enemy from a set list
    and return it to the random_battle function
    """
    bandit_loot = random.randint(10, 30)
    slime_loot = random.randint(2, 5)
    skeleton_loot = random.randint(5, 7)
    lizard_loot = random.randint(3, 10)
    bug_loot = random.randint(15, 50)
    zombie_loot = random.randint(3, 10)
    wolf_loot = random.randint(2, 5)
    goblin_loot = random.randint(5, 15)

    experience_drop = random.randint(5, 15)

    bandit = Enemy("Bandit", 20, 20, 5, 10, bandit_loot, experience_drop)
    slime = Enemy("Slime", 10, 20, 5, 2, slime_loot, experience_drop)
    skeleton = Enemy("Skeleton", 10, 20, 5, 5, skeleton_loot, experience_drop)
    lizard = Enemy("Lizard-Man", 25, 25, 8, 10, lizard_loot, experience_drop)
    bug = Enemy("Giant Bug", 30, 30, 10, 10, bug_loot, experience_drop)
    zombie = Enemy("Zombie", 20, 25, 8, 2, zombie_loot, experience_drop)
    wolf = Enemy("Wolf", 10, 20, 5, 15, wolf_loot, experience_drop)
    goblin = Enemy("Goblin", 10, 25, 6, 5, goblin_loot, experience_drop)

    if area == "Road":
        enemies = [
            bandit,
            slime,
            skeleton,
            wolf,
            goblin
        ]
    elif area == "Forest":
        enemies = [
            bandit,
            slime,
            skeleton,
            lizard,
            bug,
            zombie,
            wolf,
            goblin
        ]
    # https://stackoverflow.com/questions/306400/how-can-i-randomly-select-choose-an-item-from-a-list-get-a-random-element
    return random.choice(enemies)


def random_battle(enemy_type, encounter_chance):
    battle_chance = random.randint(0, 10)

    if battle_chance > encounter_chance:
        battle_event(adventurer, enemy_type)
        sleep(3)


def battle_event(player, enemy_type):
    """
    A function to contain battles allowing them
    to be used throughout each dungeon.
    """
    battle_loop = True

    def is_player_alive():
        """
        A simple function to check the players health and
        call the end of the game if the player health drops to 0 or below
        """
        player.check_life()
        sleep(1.5)
        if player.check_life():
            game_over()

    slow_print(f"You have encountered a {enemy_type.name}!")
    if player.speed > enemy_type.speed:
        slow_print(f"The {enemy_type.name} tried to attack you "
                   "but you were ready for it!")
        sleep(1.5)

    elif player.speed < enemy_type.speed:
        slow_print(f"The {enemy_type.name} ambushed you!")
        enemy_type.attack_other(player)
        is_player_alive()

    while battle_loop is True:
        os.system('clear')
        slow_print("You are in combat with a "
                   f"{enemy_type.name}")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Attack.")
        slow_print("2. Defend.")
        slow_print("3. Use Item.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            slow_print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()
        else:
            if choice == str(1):
                slow_print(f"You attack the {enemy_type.name}")
                player.attack_other(enemy_type)
                enemy_type.check_life()
                if enemy_type.check_life():
                    slow_print(f"You have defeated the {enemy_type.name}!")
                    enemy_type.drop_loot(adventurer, enemy_type.loot)
                    adventurer.level_up(enemy_type.experience)
                    slow_screen_clear()
                    battle_loop = False
                    break
                slow_print(f"The {enemy_type.name} counterattacks!")
                enemy_type.attack_other(player)
                is_player_alive()
                slow_screen_clear()

            elif choice == str(2):
                player.block_attack(enemy_type)
                # https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
                stun_chance = random.randrange(10)+1
                if stun_chance > 7:
                    slow_print(f"You knocked the {enemy_type.name} off balance! \
                               You strike for a counter attack!")
                    player.attack *= 1.5
                    player.attack_other(enemy_type)
                    player.attack /= 1.5
                    enemy_type.check_life()
                    if enemy_type.check_life():
                        slow_print(f"You have defeated the {enemy_type.name}!")
                        enemy_type.drop_loot(adventurer, enemy_type.loot)
                        adventurer.level_up(enemy_type.experience)
                        slow_screen_clear()
                        battle_loop = False
                    slow_screen_clear()

            elif choice == str(3):
                inventory_loop = True
                while inventory_loop is True:
                    available_items = 0
                    for number, items_owned in enumerate(adventurer.inventory):
                        slow_print(number+1, items_owned)
                        available_items += 1
                    slow_print("\nWhat would you like to use? \
                    \nPress 0 to return to the battle menu.")
                    choice = input()
                    try:
                        if choice > str(available_items) \
                         and choice.alpha() is True:
                            raise Exception

                    except Exception:
                        slow_print("Please only enter the numbers on screen, \
                        \nor 0 to return to the shop.")
                        slow_screen_clear()

                    else:
                        if choice == str(0):
                            inventory_loop = False

                        elif (choice <= str(available_items)
                              and choice > str(0)):
                            if (adventurer.inventory[int(choice)-1]
                               == "Potion"):
                                if adventurer.health < 100:
                                    adventurer.use_potion(25)
                                    adventurer.inventory.\
                                        pop(int(choice)-1)
                                    inventory_loop = False

                                else:
                                    slow_print(f"You are already at "
                                               "full health.")

                            elif (adventurer.inventory[int(choice)-1]
                                  == "Large Potion"):
                                if adventurer.health < 100:
                                    adventurer.use_potion(50)
                                    adventurer.inventory.pop(int(choice)-1)
                                    inventory_loop = False

                                else:
                                    slow_print(f"You are already at "
                                               "full health.")

                            elif (adventurer.inventory[int(choice)-1]
                                  == "Max Potion"):
                                if adventurer.health < 100:
                                    adventurer.use_potion(100)
                                    adventurer.inventory.pop(int(choice)-1)
                                    inventory_loop = False

                                else:
                                    slow_print(f"You are already at "
                                               "full health.")

                            else:
                                slow_print("Using that item will "
                                      "have no effect.")
                            slow_screen_clear()