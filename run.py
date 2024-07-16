#  Your code goes here.
#  You can delete these comments, but do not change the name of this file
#  Write your code to expect a terminal of 80 characters wide and 24 rows high

# https://www.geeksforgeeks.org/clear-screen-python/
import os
# imported to create a character by character print function
from sys import stdout
from time import sleep

# imported for battle functionality
import random


def slow_print(text, delay=0.025):
    """
    A function to print out lines character by character rather
    than having it presented immediately
    """
    # https://stackoverflow.com/questions/75486619/how-to-print-one-character-at-a-time-but-maintain-print-function-python
    if text:  # checking for text content in the provided string
        for c in text:
            print(c, end='', flush=True)
            sleep(delay)
        if text[-1] != '\n':
            print()


"""
CHARACTER CLASSES AND METHODS
"""

# move to characters.py to define protag, enemies, etc in one file.


class Character:
    """
    Creates an Instance of a Character Class.
    """

    def __init__(self, name, health, attack, defence, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed

    def attack_other(self, other_char):
        """
        A function allowing one character to reduce another characters health
        """
        damage_taken = self.attack - (other_char.defence / 2.5)
        other_char.health -= damage_taken
        slow_print(f"{other_char.name} took {damage_taken} damage!")
        if other_char.health > 0:
            slow_print(f"{other_char.name} has {other_char.health} "
                       "health remaining!")
        elif other_char.health <= 0:
            other_char.health = 0
            slow_print(f"{other_char.name} has no health remaining!")

    def check_life(self):
        """
        A simple function to check if the character still has health.
        If the health is equal to or below 0 it returns True for checks.
        """
        if self.health <= 0:
            self.health = 0
            return True

    def recover_health(self, amount):
        """
        A simple function to restore health to a character
        and prevent it from going above 100.
        """
        self.health += amount
        if self.health > 100:
            self.health = 100

    def use_potion(self, amount):
        """
        A simple function using the above recover_health() function to
        restore health and print out the results.
        """
        self.recover_health(amount)
        slow_print(f"You now have {player.health}.")
        sleep(1.5)


class Player(Character):
    """
    Creates an Instance of a Player Character Class.
    """

    def __init__(self, name, health, attack, defence,
                 speed, gold, inventory, quests):
        super().__init__(name, health, attack, defence, speed)
        self.gold = gold
        self.inventory = inventory
        self.quests = quests
        # variables used for checks through dungeons
        # will be reset to default on return to town
        # road_3 variables
        self.road3_side_road_seen = False
        self.road3_tracks_found = False
        self.road3_enemy_fought = False
        self.road3_camp_fought = False
        # road_4 variables
        self.road_4_struggle_seen = False
        self.road_4_fight = False
        self.road_4_group = False

    def block_attack(self, other_char):
        slow_print("You block the enemy attack!")
        self.defence *= 2
        other_char.attack_other(self)
        self.defence /= 2

    def reset_flags(self):
        self.road3_side_road_seen = False
        self.road3_tracks_found = False
        self.road3_enemy_fought = False
        self.road3_camp_fought = False
        self.road_4_struggle_seen = False
        self.road_4_fight = False
        self.road_4_group = False


class Enemy(Character):
    """
    Creates an Instance of an Enemy Character Class.
    """

    def __init__(self, name, health, attack, defence, speed):
        super().__init__(name, health, attack, defence, speed)

    def drop_loot(self, player, loot):
        player.gold += loot
        print(f"The {self.name} dropped {loot} gold!")


adventurer = Player("Adventurer Boy", 100, 1000, 10, 12, 1000,
                    ["Old Sword", "New Sword",  "Potion"], [])

"""
INTRO FUNCTIONS
"""

# move to intro.py


def splash_screen():
    """
    A function to display the splash screen to start, display rules,
    and end the game based on player input.
    """
    os.system('clear')
    slow_print("Averland Adventures\n")
    slow_print("A text based choose your own adventure RPG game.")
    while True:
        slow_print("What would you like to do?\n")
        slow_print("1. Start Game")
        slow_print("2. Read Rules")
        slow_print("3. Exit Game")
        try:
            choice = int(input())
            if choice != 1 and choice != 2 and choice != 3:
                raise Exception

        except Exception:
            print("Please enter only 1, 2 or 3.\n")

        else:
            if choice == 1:
                game_intro()

            elif choice == 2:
                rules()

            elif choice == 3:
                exit_game()


# move to intro.py
def rules():
    """
    A function to display rules to the player.
    """
    # https://www.geeksforgeeks.org/clear-screen-python/
    # clearing screen before presenting new lines
    os.system('clear')
    slow_print("In Averland Adventures you take on "
               "the role of a new adventurer.")
    slow_print("It will be your job to fulfill quests for the townsfolk.")
    slow_print("Slaying monsters, rescuing the innocent, "
               "recovering lost treasures.")
    slow_print("The game will be played entirely using "
               "the number keys. (1,2,3, etc.)")
    slow_print("Simply follow the on screen prompts "
               "to decide your next action.")
    slow_print("Best of luck on your quests, brave Adventurer!")
    slow_print("\nTo return to the main menu, press 1:\n")
    while True:
        go_back = int(input())
        try:
            if go_back != 1:
                raise Exception
        except Exception:
            print("Please press 1.\n")
        else:
            if go_back == 1:
                splash_screen()


# move to intro.py
def exit_game():
    """
    A function to end the game.
    """
    os.system('clear')
    slow_print("You will be missed, brave adventurer.")
    slow_print("Perhaps we shall see you again, another time.")
    slow_print("Farewell.")


# move to intro.py
def game_intro():
    """
    A function to begin the game.
    """
    os.system('clear')
    slow_print("Welcome to the kingdom of Averland, brave adventurer.")
    while True:
        slow_print("What is your name?")
        print("(Use alphabetic characters only "
              "and use less than 20 characters)")
        your_name = input()
        try:
            if your_name.isalpha() is False:
                raise Exception
            elif len(your_name) > 20:
                raise Exception
        except Exception:
            print("Please keep your name under 20 characters "
                  "and only use alphabetic characters.\n")
        else:
            adventurer = Player(your_name, 100, 10, 10, 5, 10,
                                ["Old Sword", "Old Shield"], ["Empty"])
            slow_print(f"You are {adventurer.name}! You are a brave soul "
                       "with {adventurer.health} points of health.")
            slow_print(f"{adventurer.attack} attack, {adventurer.defence} "
                       f"defence, {adventurer.speed} speed and "
                       f"{adventurer.gold} gold pieces.")
            slow_print(f"You have {adventurer.inventory} in your inventory.")
            slow_print(f"Your quest log is {adventurer.quests}... for now.")
            slow_print(f"Prepare to embark on a thrilling adventure, "
                       "in pursuit of fame and fortune, "
                       f"brave {adventurer.name}!\n")
            slow_print("...", 0.25)
            slow_print("..", 0.25)
            slow_print(".", 0.25)
            town()
            return False


def game_over():
    slow_print("Alas, brave adventurer, it seems the dangers "
               "of Averland were too great for you...")
    slow_print("Perhaps, someday, another brave soul with take "
               "up your sword and fight in your name...")
    slow_print("For now, rest... and worry not about the "
               "people of Averland any longer...")
    slow_print("...")
    while True:
        slow_print("Would you like to start again?")
        print("1. Yes")
        print("2. No")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1 or 2.\n")
        else:
            if choice == 1:
                slow_print("May your efforts bear more fruit "
                           "this time, adventurer.\n")
                game_intro()
                return False

            elif choice == 2:
                slow_print("Perhaps we shall meet again in another life.\n")
                sleep(3)
                quit()
                return False


"""
HUBWORLD FUNCTIONS
"""


# move to hubworld.py
def town():
    """
    A function to hold the Town the player will return
    to after completing each adventure.
    """
    adventurer.reset_flags()
    os.system('clear')
    slow_print("You are in town.")
    while True:
        slow_print("What would you like to do?\n")
        slow_print("1. Shop.")
        slow_print("2. Accept a quest.")
        slow_print("3. Depart on an adventure.")
        slow_print("4. Rest and end your adventures.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3 or 4.\n")
        else:
            if choice == 1:
                shop()
                return False

            elif choice == 2:
                find_a_quest()
                return False

            elif choice == 3:
                begin_adventure()
                return False

            elif choice == 4:
                os.system('clear')
                slow_print(f"Rest now, brave {adventurer.name}.")
                slow_print("Perhaps we shall see you again, another time.")
                slow_print("Farewell.")
                return False


# move to hubworld.py
def shop():
    """
    A function to hold the Shop the player can
    spend their gold or sell their items at.
    """
    # methods specific to shopping
    def buy():
        os.system('clear')
        print("You approach the shopkeep and ask what they have for sale.")
        while True:
            print("Shop selection:")
            print("1. Weapons")
            print("2. Armor")
            print("3. Items")
            print("4. Leave the shop")
            print("What would you like to do?\n")
            choice = int(input())
            try:
                if choice != 1 and choice != 2 \
                 and choice != 3 and choice != 4:
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == 1:
                    while True:
                        print("Available weapons for sale:")
                        print("1. Iron Sword: +2 Attack when "
                              "equipped. 50 gold.")
                        print("2. Steel Sword: +4 Attack when "
                              "equipped. 150 gold.")
                        print("3. Silver Sword: +6 Attack when "
                              "equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = int(input())
                        try:
                            if choice != 1 and choice != 2 \
                             and choice != 3 and choice != 4:
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == 1:
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                elif "Iron Sword" in adventurer.inventory:
                                    print("You already own an Iron Sword")
                                else:
                                    print("You have added an Iron Sword to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Iron Sword")
                            elif choice == 2:
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                elif "Steel Sword" in adventurer.inventory:
                                    print("You already own a Steel Sword")
                                else:
                                    print("You have added a Steel Sword to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Steel Sword")
                            elif choice == 3:
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                elif "Silver Sword" in adventurer.inventory:
                                    print("You already own a Silver Sword")
                                else:
                                    print("You have added a Silver Sword "
                                          "to your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Silver Sword")
                            elif choice == 4:
                                shop()
                                return False

                elif choice == 2:
                    while True:
                        print("Available armor for sale:")
                        print("1. Iron Armor: +2 Defence "
                              "when equipped. 50 gold.")
                        print("2. Steel Armor: +4 Defence "
                              "when equipped. 150 gold.")
                        print("3. Silver Armor: +6 Defence "
                              "when equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = int(input())
                        try:
                            if choice != 1 and choice != 2 \
                             and choice != 3 and choice != 4:
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == 1:
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                elif "Iron Armor" in adventurer.inventory:
                                    print("You already own Iron Armor")
                                else:
                                    print("You have added Iron Armor to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Iron Armor")
                            elif choice == 2:
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                elif "Steel Armor" in adventurer.inventory:
                                    print("You already own Steel Armor")
                                else:
                                    print("You have added Steel Armor to your "
                                          "inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Steel Armor")
                            elif choice == 3:
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                elif "Silver Armor" in adventurer.inventory:
                                    print("You already own a Silver Armor")
                                else:
                                    print("You have added Silver Armor to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Silver Armor")
                            elif choice == 4:
                                shop()
                                return False

                elif choice == 3:
                    while True:
                        print("Available items for sale:")
                        print("1. Potion. Restore 25 Health. 50 gold.")
                        print("2. Large Potion. Restore 50 Health. 150 gold.")
                        print("3. Max Potion: Fully restore Health. 300 gold.")
                        print("4. Check other options.")
                        choice = int(input())
                        try:
                            if choice != 1 and choice != 2 \
                             and choice != 3 and choice != 4:
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == 1:
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Potion")
                            elif choice == 2:
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Large Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Large Potion")
                            elif choice == 3:
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Max Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Max Potion")
                            elif choice == 4:
                                shop()
                                return False

                elif choice == 4:
                    find_a_quest()
                    return False

    def sell():
        os.system('clear')
        slow_print("You open your bag to see what you "
                   "could sell to the shopkeep.\n")
        # https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3
        while True:
            available_items = 0
            for number, items_owned in enumerate(adventurer.inventory):
                print(number+1, items_owned)
                available_items += 1
            print("What would you like to sell? "
                  "Press 0 to return to the shop.")
            choice = int(input())
            try:
                if choice > available_items and choice.alpha() is False:
                    raise Exception
            except Exception:
                print("Please only enter the numbers on screen, "
                      "or 0 to return to the shop.")
            else:
                if choice == 0:
                    shop()
                    return False
                elif choice <= available_items and choice > 0:
                    if (adventurer.inventory[choice-1] == "Iron Sword"
                       or adventurer.inventory[choice-1] == "Iron Armor"
                       or adventurer.inventory[choice-1] == "Potion"):
                        adventurer.gold += 25
                        print("You got 25 gold from selling your "
                              f"{adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)

                    elif (adventurer.inventory[choice-1] == "Steel Sword"
                          or adventurer.inventory[choice-1] == "Steel Armor"
                          or adventurer.inventory[choice-1] == "Large Potion"):
                        adventurer.gold += 50
                        print("You got 50 gold from selling your "
                              f"{adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)

                    elif (adventurer.inventory[choice-1] == "Silver Sword"
                          or adventurer.inventory[choice-1] == "Silver Armor"
                          or adventurer.inventory[choice-1] == "Max Potion"):
                        adventurer.gold += 150
                        print("You got 150 gold from selling your "
                              f"{adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)

                    else:
                        adventurer.gold += 10
                        print("You got 10 gold from selling your "
                              f"{adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)

    def leave_shop():
        os.system('clear')
        slow_print("You leave the shop and return to the center of town.\n")
        sleep(1.5)
        town()
        return False

    os.system('clear')
    slow_print("You are in the shop.")
    while True:
        slow_print("What would you like to do?\n")
        slow_print("1. Buy.")
        slow_print("2. Sell.")
        slow_print("3. Leave.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                buy()
                return False

            elif choice == 2:
                sell()
                return False

            elif choice == 3:
                leave_shop()
                return False


# move to hubworld.py
def find_a_quest():
    """
    A function to hold the tavern where the player can find new quests.
    """

    # methods specific to the tavern for quests
    def quest_board():
        os.system('clear')
        slow_print("You check the quest board for "
                   "official quests from the town guild.\n")
        while True:
            print("Currently available quests:")
            print("1. Slay 5 slimes on the Merchant Road")
            print("2. Defend a caravan on the Merchant Road")
            print("3. Clear out a bandit camp in the Forest")
            print("4. Leave the quest board")
            print("What quest will you accept?\n")
            choice = int(input())
            try:
                if choice != 1 and choice != 2 \
                 and choice != 3 and choice != 4:
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == 1:
                    if "Slay Slimes" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defeat Slimes.")
                        adventurer.quests.append("Slay Slimes")

                elif choice == 2:
                    if "Defend Caravan" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defend a merchant caravan.")
                        adventurer.quests.append("Defend Caravan")

                elif choice == 3:
                    if "Clear Bandit Camp" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "clear out a bandit camp.")
                        adventurer.quests.append("Clear Bandit Camp")
                elif choice == 4:
                    find_a_quest()
                    return False

    def ask_a_local():
        os.system('clear')
        slow_print("You ask a local and they tell you "
                   "about some jobs you could do.\n")
        while True:
            print("Currently available quests:")
            print("1. Find lost necklace on the Merchant Road")
            print("2. Person missing in the forest")
            print("3. Bandit kidnapping")
            print("4. Leave the locals")
            print("Will you offer help with any of their jobs?\n")
            choice = int(input())
            try:
                if choice != 1 and choice != 2 \
                 and choice != 3 and choice != 4:
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == 1:
                    if "Missing Necklace" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have offered to help find the necklace.")
                        adventurer.quests.append("Missing Necklace")

                elif choice == 2:
                    if "Missing Person" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "find the missing person.")
                        adventurer.quests.append("Missing Person")

                elif choice == 3:
                    if "Bandit Kidnapping" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "rescue the kidnapped person.")
                        adventurer.quests.append("Bandit Kidnapping")
                elif choice == 4:
                    find_a_quest()
                    return False

    def leave_tavern():
        os.system('clear')
        slow_print("You leave the tavern and return to the center of town.\n")
        sleep(1.5)
        town()

    os.system('clear')
    slow_print("You are in the tavern.")
    while True:
        slow_print("What would you like to do?\n")
        slow_print("1. Check the Quest Board.")
        slow_print("2. Ask a local for work.")
        slow_print("3. Leave.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                quest_board()
                return False

            elif choice == 2:
                ask_a_local()
                return False

            elif choice == 3:
                leave_tavern()
                return False


# move to hubworld.py
def begin_adventure():
    os.system('clear')
    slow_print("You set out from town.")
    while True:
        os.system('clear')
        slow_print("What is your destination?\n")
        slow_print("1. Merchant Road.")
        slow_print("2. Forest.")
        slow_print("3. Stay in Town.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                os.system('clear')
                slow_print("You travel the merchant's road.\n")
                road_start()
                return False

            elif choice == 2:
                os.system('clear')
                slow_print("You depart towards the forest\n")

            elif choice == 3:
                os.system('clear')
                slow_print("You turn around and go back to the town square.\n")
                town()
                return False


def random_enemy():
    """
    A function to select a random enemy from a set list
    and return it to the random_battle function
    """
    enemies = [
        Enemy("Bandit", 20, 10, 10, 10),
        Enemy("Slime", 10, 5, 5, 2),
        Enemy("Skeleton", 10, 10, 5, 5),
        Enemy("Lizard-Man", 15, 15, 10, 10),
        Enemy("Giant Bug", 25, 15, 15, 10),
        Enemy("Zombie", 20, 5, 10, 2),
        Enemy("Wolf", 10, 5, 5, 15)
    ]
    # https://stackoverflow.com/questions/306400/how-can-i-randomly-select-choose-an-item-from-a-list-get-a-random-element
    return random.choice(enemies)


def random_battle(enemy_type):
    battle_chance = random.randrange(10)+1

    if battle_chance > 5:
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
        slow_print("What will you do?\n")
        slow_print("1. Attack.")
        slow_print("2. Defend.")
        slow_print("3. Use Item.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            slow_print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                slow_print(f"You attack the {enemy_type.name}")
                player.attack_other(enemy_type)
                enemy_type.check_life()
                if enemy_type.check_life():
                    slow_print(f"You have defeated the {enemy_type.name}!")
                    enemy_type.drop_loot(adventurer, 10)
                    battle_loop = False
                    break
                slow_print(f"The {enemy_type.name} counterattacks!")
                enemy_type.attack_other(player)
                is_player_alive()
                sleep(1.5)

            elif choice == 2:
                player.block_attack(enemy_type)
                # https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
                stun_chance = random.randrange(10)+1
                if stun_chance > 7:
                    print(f"You knocked the {enemy_type.name} off balance! \
                    You strike for a counter attack!")
                    player.attack *= 1.5
                    player.attack_other(enemy_type)
                    player.attack /= 1.5
                    enemy_type.check_life()
                    if enemy_type.check_life():
                        print(f"You have defeated the {enemy_type.name}!")
                        enemy_type.drop_loot(adventurer, 10)
                        battle_loop = False
                    sleep(1.5)

            elif choice == 3:
                inventory_loop = True
                while inventory_loop is True:
                    available_items = 0
                    for number, items_owned in enumerate(adventurer.inventory):
                        print(number+1, items_owned)
                        available_items += 1
                    print("What would you like to use? \
                    \nPress 0 to return to the battle menu.")
                    choice = int(input())
                    try:
                        if choice > available_items \
                         and choice.alpha() is False:
                            raise Exception
                    except Exception:
                        print("Please only enter the numbers on screen, \
                        \nor 0 to return to the shop.")
                    else:
                        if choice == 0:
                            inventory_loop = False
                        elif choice <= available_items and choice > 0:
                            if adventurer.inventory[choice-1] == "Potion":
                                slow_print(f"You drink the Potion \
                                           and recover 25 health.")
                                adventurer.use_potion(25)
                                adventurer.inventory.pop(choice-1)
                                inventory_loop = False
                            elif adventurer.inventory[choice-1] \
                                    == "Large Potion":
                                slow_print(f"You drink the Large Potion \
                                           and recover 50 health.")
                                adventurer.use_potion(50)
                                adventurer.inventory.pop(choice-1)
                                inventory_loop = False
                            elif adventurer.inventory[choice-1] \
                                    == "Max Potion":
                                slow_print(f"You drink the Max Potion \
                                           and recover 100 health.")
                                adventurer.use_potion(100)
                                adventurer.inventory.pop(choice-1)
                                inventory_loop = False
                            else:
                                print("Using that item will have no effect.")


"""
MERCHANT ROAD FUNCTIONS
"""


def road_start():
    print("flavour text")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                road_1()
                return False
            elif choice == 2:
                print("flavour text for looking")
            elif choice == 3:
                print("You decide you are unprepared and return to town.")
                delay(1.5)
                town()
                return False


def road_1():
    os.system('clear')
    found_gold_road_1 = False
    slow_print("flavour text for road 1")
    sleep(1.5)
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                road_2()
                return False
            elif choice == 2:
                if found_gold_road_1 is not True:
                    print("flavour text for looking. you found gold!")
                    adventurer.gold += 10
                    found_gold_road_1 = True
                    sleep(1.5)
                else:
                    print("There is nothing else of interest.")
                    sleep(1.5)
            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_start()


def road_2():
    os.system('clear')
    slow_print("flavour text for road 2")
    sleep(1.5)
    random_battle(random_enemy())

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
              and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                sleep(1.5)
                road_3()
                return False
            elif choice == 2:
                print("There is nothing of interest.")
                sleep(1.5)
            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_1()


def road_3():
    os.system('clear')
    slow_print("flavour text for road 3")
    sleep(1.5)

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                sleep(1.5)
                road_4()
                return False

            elif choice == 2:
                if adventurer.road3_side_road_seen is False:
                    adventurer.road3_side_road_seen = True
                    slow_print("You notice there is a path "
                               "leading through some bushes.")
                elif adventurer.road3_side_road_seen is True:
                    slow_print("You consider the path you "
                               "noticed earlier.")
                slow_print("Would you like to investigate "
                           "this side road?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = int(input())
                try:
                    if choice != 1 and choice != 2:
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == 1:
                        slow_print("You decide to travel the side road.")
                        sleep(1.5)
                        road_3a()
                        return False

                    elif choice == 2:
                        slow_print("You decide it safer to stick "
                                   "to the path more trodden.")
                        sleep(1.5)

            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_2()


def road_3a():
    os.system('clear')
    slow_print("This is Placeholder text for 3a")
    sleep(1.5)

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                print("You go back to the main road.")
                sleep(1.5)
                road_3()
                return False

            elif choice == 2:
                if adventurer.road3_tracks_found is False:
                    adventurer.road3_tracks_found = True
                    slow_print("You find some tracks in the "
                               "dirt at your feet.")
                elif adventurer.road3_tracks_found is True:
                    slow_print("You consider the tracks "
                               "you found earlier.")
                slow_print("Would you like to "
                           "follow them?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = int(input())
                try:
                    if choice != 1 and choice != 2:
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == 1:
                        slow_print("You decide to follow the tracks "
                                   "further off the road.")
                        sleep(1.5)
                        road_3b()
                        return False

                    elif choice == 2:
                        slow_print("You aren't sure what may be at "
                                   "the end of these tracks,\n so you "
                                   "err on the side of caution.")
                        sleep(1.5)


def road_3b():
    os.system('clear')
    slow_print("You follow the tracks through the bushes.")
    sleep(1.5)

    # generating a random enemy and assigning it to a variable
    # within the Player class to be stored for consistent encounters
    if adventurer.road3_enemy_fought is False:
        adventurer.road3_enemies = random_enemy()
        battle_event(adventurer, adventurer.road3_enemies)
        adventurer.road3_enemy_fought = True
        slow_print("After the battle you realise that there must "
                   "be a group up ahead. It would be dangerous "
                   "to proceed...")
        sleep(1.5)

    else:
        slow_print(f"The body of the {adventurer.road3_enemies.name} "
                   "you defeated is still here.")

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Enter the {adventurer.road3_enemies.name}'s "
                   "territory.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                print("You go back through the bushes.")
                sleep(1.5)
                road_3a()
                return False

            elif choice == 2:
                if adventurer.road3_camp_fought is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                sleep(1.5)
                road_3c()
                return False


def road_3c():
    os.system('clear')
    if adventurer.road3_camp_fought is False:
        slow_print("As you thought there are multiple "
                   f"{adventurer.road3_enemies.name}s here.")
        sleep(1.5)
        adventurer.road3_enemies.health += 30
        adventurer.road3_enemies.attack += 10
        adventurer.road3_enemies.name += " Group"
        battle_event(adventurer, adventurer.road3_enemies)
        adventurer.road3_camp_fought = True

        slow_print("After the battle you search around the area.")
        slow_print("With nothing else of value to find you return "
                   "to the main road, triumphant.")

    else:
        slow_print("The area is silent now that you have "
                   "defeated all the enemies here.")
        slow_print("You turn around and walk back towards "
                   "the main road.")
    sleep(1.5)
    road_3()


def road_4():
    os.system('clear')
    slow_print("Placeholder text for road 4.")

    random_battle(random_enemy())

    sleep(1.5)

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                sleep(1.5)
                road_5()
                return False

            elif choice == 2:
                if adventurer.road_4_struggle_seen is False:
                    adventurer.road_4_struggle_seen = True
                    slow_print("You notice signs of a "
                               "battle leading off the road.")
                elif adventurer.road_4_struggle_seen is True:
                    slow_print("You consider the signs of "
                               "a struggle you saw earlier.")
                slow_print("Would you like to investigate?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = int(input())
                try:
                    if choice != 1 and choice != 2:
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == 1:
                        slow_print("You decide to follow the damage.")
                        sleep(1.5)
                        road_4a()
                        return False

                    elif choice == 2:
                        slow_print("It could be a trap.\n You decide"
                                   "to stay on the main road.")
                        sleep(1.5)

            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_3()


def road_4a():
    os.system('clear')
    slow_print("You follow the evidence of a struggle further off the road.")
    sleep(1.5)

    if adventurer.road_4_fight is False:
        adventurer.road4_enemies = random_enemy()
        battle_event(adventurer, adventurer.road4_enemies)
        adventurer.road4_enemy_fought = True
        slow_print("After the battle placeholder")
        sleep(1.5)

    else:
        slow_print(f"The body of the {adventurer.road4_enemies.name} "
                   "you defeated is still here.")

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Go further.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                print("You go back to the main road.")
                sleep(1.5)
                road_4()
                return False

            elif choice == 2:
                if adventurer.road_4_group is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                sleep(1.5)
                road_4b()
                return False


def road_4b():
    os.system('clear')
    if adventurer.road_4_group is False:
        slow_print("As you thought there are multiple "
                   f"{adventurer.road4_enemies.name}s here.")
        sleep(1.5)
        adventurer.road4_enemies.health += 30
        adventurer.road4_enemies.attack += 10
        adventurer.road4_enemies.name += " Group"
        battle_event(adventurer, adventurer.road4_enemies)
        adventurer.road_4_group = True

        slow_print("After the battle you search around the area.")
        slow_print("With nothing else of value to find you return "
                   "to the main road, triumphant.")

    else:
        slow_print("The area is silent now that you have "
                   "defeated all the enemies here.")
        slow_print("You turn around and walk back towards "
                   "the main road.")
    sleep(1.5)
    road_4()


def road_5():
    os.system('clear')
    slow_print("flavour text for road 5")
    sleep(1.5)
    random_battle(random_enemy())

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                sleep(1.5)
                road_6()
                return False
            elif choice == 2:
                print("There is nothing of interest.")
                sleep(1.5)
            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_4()


def road_6():
    os.system('clear')
    slow_print("flavour text for road 6")
    sleep(1.5)
    random_battle(random_enemy())

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue down the road.")
                sleep(1.5)
                road_7()
                return False
            elif choice == 2:
                print("There is nothing of interest.")
                sleep(1.5)
            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_5()


def road_7():
    os.system('clear')
    slow_print("flavour text for road 5")
    sleep(1.5)

    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue towards town.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                print("You continue and arrive at the next town.")
                sleep(1.5)
                town()
                return False
            elif choice == 2:
                print("There is nothing of interest.")
                sleep(1.5)
            elif choice == 3:
                slow_print("You make your way back the way you came.")
                sleep(1.5)
                road_6()


"""
FOREST EVENTS
"""


def forest_start():
    slow_print("flavour text for forest start")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room1a()
                return False
            elif choice == 2:
                print("flavour text for looking")
            elif choice == 3:
                print("You decide you are unprepared and return to town.")
                delay(1.5)
                town()
                return False
    # leads to forest1a


def forest_room1a():
    slow_print("flavour text for room 1a")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North.") # 2a
        slow_print("2. Go West") # 1b
        slow_print("3. Go South.") # forest start
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3 or 4.\n")
        else:
            if choice == 1:
                forest_room2a()
                return False
            elif choice == 2:
                forest_room1b()
                return False
            elif choice == 3:
                forest_start()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")


def forest_room1b():
    slow_print("flavour text for room 1b")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North.") # 2b
        slow_print("2. Go East") # 1a
        slow_print("3. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room2b()
                return False
            elif choice == 2:
                forest_room1a()
                return False
            elif choice == 3:
                slow_print("flavour text for looking")
    # forest 1a or 2b


def forest_room1c():
    slow_print("flavour text for room 1c")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North.") # 2c
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                forest_room2c()
                return False
            elif choice == 2:
                slow_print("flavour text for looking")
    # forest 2c


def forest_room2a():
    slow_print("flavour text for room 2a")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go West.") # 2b
        slow_print("2. Go East") # 2c
        slow_print("3. Go South.") # 1a
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == 1:
                forest_room2b()
                return False
            elif choice == 2:
                forest_room2c()
                return False
            elif choice == 3:
                forest_room1a()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")
    # forest 1a, 2b, 2c


def forest_room2b():
    slow_print("flavour text for room 2b")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North.") # 3b
        slow_print("2. Go East") # 2a
        slow_print("3. Go South.") # 1b
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == 1:
                forest_room3b()
                return False
            elif choice == 2:
                forest_room2a()
                return False
            elif choice == 3:
                forest_room1b()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")
    # forest 2a or 3b


def forest_room2c():
    slow_print("flavour text for room 2c")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go West") # 2a
        slow_print("2. Go South.") # 1c
        slow_print("3. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room2a()
                return False
            elif choice == 2:
                forest_room1c()
                return False
            elif choice == 3:
                slow_print("flavour text for looking")
    # forest 2a or 1c


def forest_room3a():
    slow_print("flavour text for room 3a")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go East") # 3c
        slow_print("2. Go West.") # 3b
        slow_print("3. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room3c()
                return False
            elif choice == 2:
                forest_room3b()
                return False
            elif choice == 3:
                slow_print("flavour text for looking")
    # forst 3b or 3c


def forest_room3b():
    slow_print("flavour text for room 3b")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 4b
        slow_print("2. Go East.") # 3a
        slow_print("3. Go South.") # 2b
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == 1:
                forest_room4b()
                return False
            elif choice == 2:
                forest_room3a()
                return False
            elif choice == 3:
                forest_room2b()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")
    # forest 4b or 3a


def forest_room3c():
    slow_print("flavour text for room 3c")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 4c
        slow_print("2. Go West.") # 3a
        slow_print("3. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room4c()
                return False
            elif choice == 2:
                forest_room3a()
                return False
            elif choice == 3:
                slow_print("flavour text for looking")
    # forest 4c


def forest_room4b():
    slow_print("flavour text for room 4b")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North.") # 3b
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                forest_room3b()
                return False
            elif choice == 2:
                slow_print("flavour text for looking")
    # forest 3b


def forest_room4c():
    slow_print("flavour text for room 4c")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 5c
        slow_print("2. Go South.") # 3c
        slow_print("3. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == 1:
                forest_room5c()
                return False
            elif choice == 2:
                forest_room3c()
                return False
            elif choice == 3:
                slow_print("flavour text for looking")
    # forest 5c


def forest_room5a():
    slow_print("flavour text for room 5a")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 6a
        slow_print("2. Go East.") # 5c
        slow_print("3. Go West.") # 5b
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == 1:
                forest_room6a()
                return False
            elif choice == 2:
                forest_room5c()
                return False
            elif choice == 3:
                forest_room5b()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")
    # forest 5c, 5b, or 6a


def forest_room5b():
    slow_print("flavour text for room 5b")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go East.") # 5a
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                forest_room5a()
                return False
            elif choice == 2:
                slow_print("flavour text for looking")
    # forest 5a


def forest_room5c():
    slow_print("flavour text for room 5c")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 6c
        slow_print("2. Go West.") # 5a
        slow_print("3. Go South.") # 4c
        slow_print("4. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2 \
             and choice != 3 and choice != 4:
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == 1:
                forest_room6c()
                return False
            elif choice == 2:
                forest_room5a()
                return False
            elif choice == 3:
                forest_room4c()
                return False
            elif choice == 4:
                slow_print("flavour text for looking")
    # forest 5a or 6c


def forest_room6a():
    pass
    # forest 7


def forest_room6c():
    pass
    # forest 5c


def forest_room7():
    pass
    # end


def main():
    """
    Runs the primary functions for the game.
    """
    # splash_screen()
    road_start()


main()
