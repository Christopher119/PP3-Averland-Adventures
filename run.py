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

# imported to prevent words from breaking when printed to terminal
import textwrap

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


def slow_screen_clear():
    sleep(2)
    os.system('clear')


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
        self.keyitems = []
        # variables used for checks through dungeons
        # will be reset to default on return to town
        # road variables
        self.found_gold_road_1 = False
        # road_3 variables
        self.road3_side_road_seen = False
        self.road3_tracks_found = False
        self.road3_enemy_fought = False
        self.road3_camp_fought = False
        # road_4 variables
        self.road_4_struggle_seen = False
        self.road_4_fight = False
        self.road_4_group = False

        #forest variables
        self.forest1b_gold_found = False
        self.forest3a_camp = False
        self.forest3c_camp_enemy = 0
        self.room4bitem = False
        self.necklace_found = False
        self.forest_6c_camp = False

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

    def __init__(self, name, health, attack, defence, speed, loot):
        super().__init__(name, health, attack, defence, speed)
        self.loot = loot

    def drop_loot(self, player, loot):
        player.gold += self.loot
        print(f"The {self.name} dropped {self.loot} gold!")


adventurer = Player("Adventurer Boy", 100, 1000, 10, 12, 1000,
                    ["Old Sword", "New Sword",  "Potion"], [])
bandit = Enemy("Bandit", 20, 10, 10, 10, 10)

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
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3 or 4.\n")
        else:
            if choice == str(1):
                shop()
                return False

            elif choice == str(2):
                find_a_quest()
                return False

            elif choice == str(3):
                begin_adventure()
                return False

            elif choice == str(4):
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
            choice = input()
            try:
                if choice != str(1) and choice != str(2) \
                 and choice != str(3) and choice != str(4):
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == str(1):
                    while True:
                        print("Available weapons for sale:")
                        print("1. Iron Sword: +2 Attack when "
                              "equipped. 50 gold.")
                        print("2. Steel Sword: +4 Attack when "
                              "equipped. 150 gold.")
                        print("3. Silver Sword: +6 Attack when "
                              "equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if choice != str(1) and choice != str(2) \
                             and choice != str(3) and choice != str(4):
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == str(1):
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                elif "Iron Sword" in adventurer.inventory:
                                    print("You already own an Iron Sword")
                                else:
                                    print("You have added an Iron Sword to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Iron Sword")
                            elif choice == str(2):
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                elif "Steel Sword" in adventurer.inventory:
                                    print("You already own a Steel Sword")
                                else:
                                    print("You have added a Steel Sword to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Steel Sword")
                            elif choice == str(3):
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                elif "Silver Sword" in adventurer.inventory:
                                    print("You already own a Silver Sword")
                                else:
                                    print("You have added a Silver Sword "
                                          "to your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Silver Sword")
                            elif choice == str(4):
                                shop()
                                return False

                elif choice == str(2):
                    while True:
                        print("Available armor for sale:")
                        print("1. Iron Armor: +2 Defence "
                              "when equipped. 50 gold.")
                        print("2. Steel Armor: +4 Defence "
                              "when equipped. 150 gold.")
                        print("3. Silver Armor: +6 Defence "
                              "when equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if choice != str(1) and choice != str(2) \
                             and choice != str(3) and choice != str(4):
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == str(1):
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                elif "Iron Armor" in adventurer.inventory:
                                    print("You already own Iron Armor")
                                else:
                                    print("You have added Iron Armor to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Iron Armor")
                            elif choice == str(2):
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                elif "Steel Armor" in adventurer.inventory:
                                    print("You already own Steel Armor")
                                else:
                                    print("You have added Steel Armor to your "
                                          "inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Steel Armor")
                            elif choice == str(3):
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                elif "Silver Armor" in adventurer.inventory:
                                    print("You already own a Silver Armor")
                                else:
                                    print("You have added Silver Armor to "
                                          "your inventory. Remember to "
                                          "equip it.")
                                    adventurer.inventory.append("Silver Armor")
                            elif choice == str(4):
                                shop()
                                return False

                elif choice == str(3):
                    while True:
                        print("Available items for sale:")
                        print("1. Potion. Restore 25 Health. 50 gold.")
                        print("2. Large Potion. Restore 50 Health. 150 gold.")
                        print("3. Max Potion: Fully restore Health. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if choice != str(1) and choice != str(2) \
                             and choice != str(3) and choice != str(4):
                                raise Exception
                        except Exception:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if choice == str(1):
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Potion")
                            elif choice == str(2):
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Large Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Large Potion")
                            elif choice == str(3):
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Max Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Max Potion")
                            elif choice == str(4):
                                shop()
                                return False

                elif choice == str(4):
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
            choice = input()
            try:
                if choice > str(available_items) and choice.alpha() is True:
                    raise Exception
            except Exception:
                print("Please only enter the numbers on screen, "
                      "or 0 to return to the shop.")
            else:
                if choice == str(0):
                    shop()
                    return False
                elif choice <= str(available_items) and choice > str(0):
                    if (adventurer.inventory[int(choice)-1] == "Iron Sword"
                       or adventurer.inventory[int(choice)-1] == "Iron Armor"
                       or adventurer.inventory[int(choice)-1] == "Potion"):
                        adventurer.gold += 25
                        print("You got 25 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

                    elif (adventurer.inventory[int(choice)-1] == "Steel Sword"
                          or adventurer.inventory[int(choice)-1] == "Steel Armor"
                          or adventurer.inventory[int(choice)-1] == "Large Potion"):
                        adventurer.gold += 50
                        print("You got 50 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

                    elif (adventurer.inventory[int(choice)-1] == "Silver Sword"
                          or adventurer.inventory[int(choice)-1] == "Silver Armor"
                          or adventurer.inventory[int(choice)-1] == "Max Potion"):
                        adventurer.gold += 150
                        print("You got 150 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

                    else:
                        adventurer.gold += 10
                        print("You got 10 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

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
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                buy()
                return False

            elif choice == str(2):
                sell()
                return False

            elif choice == str(3):
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
            print("1. Slay 5 slimes")
            print("2. Defend a caravan on the Merchant Road")
            print("3. Clear out a bandit camp in the Forest")
            print("4. Leave the quest board")
            print("What quest will you accept?\n")
            choice = input()
            try:
                if choice != str(1) and choice != str(2) \
                 and choice != str(3) and choice != str(4):
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == str(1):
                    if "Slay Slimes" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defeat Slimes.")
                        adventurer.quests.append("Slay Slimes")

                elif choice == str(2):
                    if "Defend Caravan" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defend a merchant caravan.")
                        adventurer.quests.append("Defend Caravan")

                elif choice == str(3):
                    if "Clear Bandit Camp" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "clear out a bandit camp.")
                        adventurer.quests.append("Clear Bandit Camp")
                elif choice == str(4):
                    find_a_quest()
                    return False

    def ask_a_local():
        os.system('clear')
        slow_print("You ask a local and they tell you "
                   "about some jobs you could do.\n")
        while True:
            print("Currently available quests:")
            print("1. Find lost necklace")
            print("2. Person missing")
            print("3. Bandit kidnapping")
            print("4. Leave the locals")
            print("Will you offer help with any of their jobs?\n")
            choice = input()
            try:
                if choice != str(1) and choice != str(2) \
                 and choice != str(3) and choice != str(4):
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if choice == str(1):
                    if "Missing Necklace" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have offered to help find the necklace.")
                        adventurer.quests.append("Missing Necklace")

                elif choice == str(2):
                    if "Missing Person" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "find the missing person.")
                        adventurer.quests.append("Missing Person")

                elif choice == str(3):
                    if "Bandit Kidnapping" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "rescue the kidnapped person.")
                        adventurer.quests.append("Bandit Kidnapping")
                elif choice == str(4):
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
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                quest_board()
                return False

            elif choice == str(2):
                ask_a_local()
                return False

            elif choice == str(3):
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
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                os.system('clear')
                slow_print("You travel the merchant's road.\n")
                road_start()
                return False

            elif choice == str(2):
                os.system('clear')
                slow_print("You depart towards the forest\n")

            elif choice == str(3):
                os.system('clear')
                slow_print("You turn around and go back to the town square.\n")
                town()
                return False


#battle functions
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

    bandit = Enemy("Bandit", 20, 10, 10, 10, bandit_loot)
    slime = Enemy("Slime", 10, 5, 5, 2, slime_loot)
    skeleton = Enemy("Skeleton", 10, 10, 5, 5, skeleton_loot)
    lizard = Enemy("Lizard-Man", 15, 15, 10, 10, lizard_loot)
    bug = Enemy("Giant Bug", 25, 15, 15, 10, bug_loot)
    zombie = Enemy("Zombie", 20, 5, 10, 2, zombie_loot)
    wolf = Enemy("Wolf", 10, 5, 5, 15, wolf_loot)
    goblin = Enemy("Goblin", 10, 10, 10, 5, goblin_loot)

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
        slow_print("What will you do?\n")
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
        else:
            if choice == str(1):
                slow_print(f"You attack the {enemy_type.name}")
                player.attack_other(enemy_type)
                enemy_type.check_life()
                if enemy_type.check_life():
                    slow_print(f"You have defeated the {enemy_type.name}!")
                    enemy_type.drop_loot(adventurer, enemy_type.loot)
                    slow_screen_clear()
                    battle_loop = False
                    break
                slow_print(f"The {enemy_type.name} counterattacks!")
                enemy_type.attack_other(player)
                is_player_alive()
                sleep(1.5)

            elif choice == str(2):
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
                        enemy_type.drop_loot(adventurer, enemy_type.loot)
                        slow_screen_clear()
                        battle_loop = False
                    sleep(1.5)

            elif choice == str(3):
                inventory_loop = True
                while inventory_loop is True:
                    available_items = 0
                    for number, items_owned in enumerate(adventurer.inventory):
                        print(number+1, items_owned)
                        available_items += 1
                    print("What would you like to use? \
                    \nPress 0 to return to the battle menu.")
                    choice = input()
                    try:
                        if choice > str(available_items) \
                         and choice.alpha() is True:
                            raise Exception
                    except Exception:
                        print("Please only enter the numbers on screen, \
                        \nor 0 to return to the shop.")
                    else:
                        if choice == str(0):
                            inventory_loop = False
                        elif choice <= str(available_items) and choice > str(0):
                            if adventurer.inventory[int(choice)-1] == "Potion":
                                if adventurer.health < 100:
                                    slow_print(f"You drink the Potion "
                                                "and recover 25 health.")
                                    adventurer.use_potion(25)
                                    adventurer.inventory.pop(int(choice)-1)
                                    inventory_loop = False
                                else:
                                    slow_print(f"You are already at "
                                                "full health.")
                            elif adventurer.inventory[int(choice)-1] \
                                    == "Large Potion":
                                if adventurer.health < 100:
                                    slow_print(f"You drink the Large Potion "
                                                "and recover 50 health.")
                                    adventurer.use_potion(50)
                                    adventurer.inventory.pop(int(choice)-1)
                                    inventory_loop = False
                                else:
                                    slow_print(f"You are already at "
                                                "full health.")
                            elif adventurer.inventory[int(choice)-1] \
                                    == "Max Potion":
                                if adventurer.health < 100:
                                    slow_print(f"You drink the Max Potion "
                                                "and recover 100 health.")
                                    adventurer.use_potion(100)
                                    adventurer.inventory.pop(int(choice)-1)
                                    inventory_loop = False
                                else:
                                    slow_print(f"You are already at "
                                                "full health.")
                            else:
                                print("Using that item will have no effect.")
                            slow_screen_clear()


"""
MERCHANT ROAD FUNCTIONS
"""


def road_start():
    
    while True:
        slow_print("The wall of the town is at your back as "
                   "you begin travelling the Merchant's Road.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_1()
                return False
            elif choice == str(2):
                print("It is a peaceful and pleasant day, perfect for a "
                      "leisurely walk.\nThough something tells you that "
                      "you won't have a relaxing journey.")
                slow_screen_clear()
            elif choice == str(3):
                print("You decide you are unprepared and return to town.")
                slow_screen_clear()
                town()
                return False


def road_1():
    while True:
        slow_print("You walk at a brisk pace, enjoying the refreshing air.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_2()
                return False
            elif choice == str(2):
                if adventurer.found_gold_road_1 is not True:
                    slow_print("Your eyes scan over the road when you notice "
                               "\na small bag discarded on the roadside. You "
                               "crouch down to examine it,\nfinding it mostly "
                               "empty, save for a few coins.\nYou found 10 gold!")
                    adventurer.gold += 10
                    adventurer.found_gold_road_1 = True
                    slow_screen_clear()
                else:
                    slow_print("You see nothing else of interest.")
                    slow_screen_clear()
            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_start()
                return False


def road_2():
    random_battle(random_enemy("Road"), 7)

    while True:
        slow_print("You stay wary the further you get from a town.\n"
                   "Though merchant roads are well travelled, they "
                   "\nare also often targeted by many thieves and "
                   "monsters for that same reason.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
              and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_3()
                return False
            elif choice == str(2):
                slow_print("You wave to some passing merchants "
                           "as they head toward town.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_1()
                return False


def road_3():
    while True:
        slow_print("You keep your hand on the hilt of your "
                   "weapon, wary for any potential threats.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_4()
                return False

            elif choice == str(2):
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
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == str(1):
                        slow_print("You decide to travel the side road.")
                        slow_screen_clear()
                        road_3a()
                        return False

                    elif choice == str(2):
                        slow_print("You decide it safer to stick "
                                   "to the path more trodden.")
                        slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_2()
                return False


def road_3a():
    while True:
        slow_print("You move through some bushes warily.")
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print("2. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == str(1):
                slow_print("You go back to the main road.")
                slow_screen_clear()
                road_3()
                return False

            elif choice == str(2):
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
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == str(1):
                        slow_print("You decide to follow the tracks "
                                   "further off the road.")
                        slow_screen_clear()
                        road_3b()
                        return False

                    elif choice == str(2):
                        slow_print("You aren't sure what may be at "
                                   "the end of these tracks,\n so you "
                                   "err on the side of caution.")
                        slow_screen_clear()


def road_3b():
    slow_print("You follow the tracks through the bushes.")

    # generating a random enemy and assigning it to a variable
    # within the Player class to be stored for consistent encounters
    if adventurer.road3_enemy_fought is False:
        adventurer.road3_enemies = random_enemy("Road")
        battle_event(adventurer, adventurer.road3_enemies)
        adventurer.road3_enemy_fought = True
        slow_print("After the battle you realise that there must "
                   "be a group up ahead. It would be dangerous "
                   "to proceed...")

    else:
        slow_print(f"The body of the {adventurer.road3_enemies.name} "
                   "you defeated is still here.")

    while True:
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Enter the {adventurer.road3_enemies.name}'s "
                   "territory.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == str(1):
                print("You go back through the bushes.")
                slow_screen_clear()
                road_3a()
                return False

            elif choice == str(2):
                if adventurer.road3_camp_fought is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                slow_screen_clear()
                road_3c()
                return False


def road_3c():
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
    slow_screen_clear()
    road_3()


def road_4():

    random_battle(random_enemy("Road"), 5)

    while True:
        slow_print("You check your map as you walk,\n"
                   "estimating you are about halfway\n"
                   "to the next town.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_5()
                return False

            elif choice == str(2):
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
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                else:
                    if choice == str(1):
                        slow_print("You decide to follow the damage.")
                        slow_screen_clear()
                        road_4a()
                        return False

                    elif choice == str(2):
                        slow_print("It could be a trap.\n You decide"
                                   "to stay on the main road.")
                        slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_3()
                return False


def road_4a():
    slow_print("You follow the evidence of a struggle further off the road.")
    sleep(1.5)

    if adventurer.road_4_fight is False:
        adventurer.road4_enemies = random_enemy("Road")
        battle_event(adventurer, adventurer.road4_enemies)
        adventurer.road4_enemy_fought = True
        slow_print("After the battle placeholder")

    else:
        slow_print(f"The body of the {adventurer.road4_enemies.name} "
                   "you defeated is still here.")

    while True:
        slow_print("What will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Go further.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == str(1):
                print("You go back to the main road.")
                slow_screen_clear()
                road_4()
                return False

            elif choice == str(2):
                if adventurer.road_4_group is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                slow_screen_clear()
                road_4b()
                return False


def road_4b():
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
    slow_screen_clear()
    road_4()


def road_5():
    random_battle(random_enemy("Road"), 3)

    while True:
        slow_print("You pause for a moment of rest on the side of the road,\n"
                   "keeping a careful watch for any threats.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                print("You continue down the road.")
                slow_screen_clear()
                road_6()
                return False
            elif choice == str(2):
                print("Nothing catches your eye.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_4()
                return False


def road_6():

    random_battle(random_enemy("Road"), 2)

    while True:
        slow_print("The road is getting a little busier, more merchants,\n"
                   "but also more possible threats lying in wait ahead.")
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_7()
                return False
            elif choice == str(2):
                slow_print("There is nothing of interest.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_5()
                return False


def road_7():
    while True:
        slow_print("As you walk the road you see the next town not far from you.")
        slow_print("What will you do?\n")
        slow_print("1. Continue towards town.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue and arrive at the next town.")
                slow_screen_clear()
                town()
                return False
            elif choice == str(2):
                slow_print("There is nothing of interest.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_6()
                return False


"""
FOREST EVENTS
"""


def forest_start():
    while True:
        slow_print("You arrive at the entrance to the nearby forest.\n"
                   "Tales of monsters dens and hidden riches bid many\n"
                   "adventurer to tackle it.\n")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Head deeper into the forest.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.")
            slow_screen_clear()
        else:
            if choice == str(1):
                slow_print("You press through the trees and bushes")
                slow_screen_clear()
                forest_room1a()
                return False
            elif choice == str(2):
                slow_print("The canopy of trees obscures much of the light "
                           "from the sun,\nallowing only a few dappled rays "
                           "to shine through. There is a\nsmall road leading "
                           "into the forest proper that you can follow\n"
                           "for a certain distance.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("You decide you are unprepared and return to town.")
                slow_screen_clear()
                town()
                return False


def forest_room1a():
    while True:
        slow_print("A few animals dash into the bushes\n"
                   "as you walk into a small clearing.")
        slow_print("What will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go West")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            slow_print("Please enter only 1, 2, 3 or 4.")
        else:
            if choice == str(1):
                slow_print("You head north.")
                slow_screen_clear()
                forest_room2a()
                return False
            elif choice == str(2):
                slow_print("You head west.")
                slow_screen_clear()
                forest_room1b()
                return False
            elif choice == str(3):
                slow_print("You head south.")
                slow_screen_clear()
                forest_start()
                return False
            elif choice == str(4):
                slow_print("The bushes rustle as some critters scurry"
                           "around in the underbrush.")
                slow_screen_clear()


def forest_room1b():
    
    while True:
        slow_print("Some birds are chirping nearby as you \n"
                   "make your way through the dense foliage.")
        slow_print("What will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go East")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You head north.")
                slow_screen_clear()
                forest_room2b()
                return False
            elif choice == str(2):
                slow_print("You head west.")
                slow_screen_clear()
                forest_room1a()
                return False
            elif choice == str(3):
                if adventurer.forest1b_gold_found is False:
                    slow_print("You notice something glittering "
                               "in the grass at your feet.")
                    slow_print("You found 5 gold coins!")
                    adventurer.gold += 5
                else:
                    slow_print("You find nothing else of interest.")
                slow_screen_clear()


def forest_room1c():
    while True:
        slow_print("The air suddenly feels lighter as you "
                   "come across a \nsmall spring. The water "
                   "seems to shimmer as you look at it.")
        slow_print("What will you do?\n")
        slow_print("1. Go back the way you came.")
        slow_print("2. Drink from the spring.")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You turn around and leave the "
                           "small spring behind you.")
                slow_screen_clear()
                forest_room2c()
                return False
            elif choice == str(2):
                slow_print("You kneel by the edge of the water, "
                           "scooping a handful \nof it into your mouth."
                           "You feel invigorated as you drink it!")
                adventurer.recover_health(20)
                slow_print("You have recovered 20 hp!")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("The area seems to almost shine with "
                           "a mystical glow.")
                slow_screen_clear()


def forest_room2a():

    random_battle(random_enemy("Forest"), 5)

    while True:
        slow_print("Your tunic tears on a sharp branch as "
                   "you walk deeper into the forest.")
        slow_print("What will you do?\n")
        slow_print("1. Go West.")
        slow_print("2. Go East")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == str(1):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room2b()
                return False
            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room2c()
                return False
            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room1a()
                return False
            elif choice == str(4):
                slow_print("There are strange markings on some of the trees. \n"
                           "Perhaps territorial warning signs from some \n"
                           "bandits or monsters.")
    # forest 1a, 2b, 2c


def forest_room2b():

    random_battle(random_enemy("Forest"), 3)

    while True:
        slow_print("The trees are particularly dense in this part of the \n"
                   "forest, making it difficult to move quickly.")
        slow_print("What will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go East")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room3b()
                return False
            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room2a()
                return False
            elif choice == str(3):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room1b()
                return False
            elif choice == str(4):
                slow_print("You notice more of those marking on the "
                           "trees as you move between them.")


def forest_room2c():
    while True:
        slow_print("The forest seems strangely quiet now... \n"
                   "Perhaps there is a danger ahead?")
        slow_print("What will you do?\n")
        slow_print("1. Go West")
        slow_print("2. Go South.")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room2a()
                return False
            elif choice == str(2):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room1c()
                return False
            elif choice == str(3):
                slow_print("You can't see anything out of the ordinary "
                           "\nunder the shade of the forest canopy.")


def forest_room3a():
    if adventurer.forest3a_camp is False:
        forest_room3a_campfight()
    
    else:
        forest_room3a_campdefeat()


def forest_room3a_campfight():
    while True:
        adventurer.forest3c_camp_enemy = random_enemy("Forest")
        adventurer.forest3c_camp_enemy.name += " Group"
        slow_print("You press up against a tree as you hear "
                   "noises ahead.\nYou peer around the "
                   "trunk and notice some shadows moving \n"
                   "just up ahead. It may be a group "
                   "of monsters...")
                       
        slow_print("What will you do?\n")
        slow_print("1. Try to sneak past.")
        slow_print("2. Step into the open.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1 or 2.\n")
        else:
            if choice == str(1):
                if adventurer.speed > random.randint(7, 13):
                    slow_print("You successfully skirt your "
                               "way past the group.")
                    forest_room3a_campdefeat()
                    return False
                else:
                    slow_print("A cry yells out followed by "
                               "a rush of movement!")
                    slow_print("You've been seen! "
                               "Prepare to fight!")
                    adventurer.forest3c_camp_enemy.health += 30
                    adventurer.forest3c_camp_enemy.attack += 15
                    random_battle(adventurer.forest3c_camp_enemy, -1)
                    adventurer.forest3a_camp = True
                    forest_room3a_campdefeat()
                    return False

            elif choice == str(2):
                slow_print("You sneak closer and see a "
                           f"{adventurer.forest3c_camp_enemy.name} \n"
                           "gathered up ahead.\nYou manage to "
                           "take one out before the group notices.")
                slow_print("Prepare to fight!")
                adventurer.forest3c_camp_enemy.health += 20
                adventurer.forest3c_camp_enemy.attack += 10
                random_battle(adventurer.forest3c_camp_enemy, -1)
                adventurer.forest3a_camp = True
                forest_room3a_campdefeat()
                return False


def forest_room3a_campdefeat():
    while True:
        if adventurer.forest3a_camp is True:
            slow_print("The bodies of the "
                       f"{adventurer.forest3c_camp_enemy.name}"
                       " lay on the ground where you defeated them.")
        else:
            slow_print("The noise from the nearby group "
                       "slowly fades as you sneak away.")
                    
        slow_print("What will you do?\n")
        slow_print("1. Go East")
        slow_print("2. Go West.")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
            and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room3c()
                return False
            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room3b()
                return False
            elif choice == str(3):
                slow_print("There is an array of scattered objects on "
                           "the ground, no doubt from that group.")


def forest_room3b():

    random_battle(random_enemy("Forest"), 6)

    while True:
        slow_print("A sweet scent reaches your nose as you push "
                   "through some bushes. Perhaps there is a fresh flower "
                   "blooming nearby.")
        slow_print("What will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go East.")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room4b()
                return False
            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room3a()
                return False
            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room2b()
                return False
            elif choice == str(4):
                slow_print("You see a flowerbed blooming under "
                           "the shade of a fallen log.")


def forest_room3c():

    random_battle(random_enemy("Forest"), 3)

    while True:
        slow_print("The forest is getting denser the deeper you go. \n"
                   "It looks like there's only one path forward.")
        slow_print("What will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go West.")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room4c()
                return False
            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room3a()
                return False
            elif choice == str(3):
                slow_print("You could almost swear there are... faces\n "
                           "in the bark of the trees. All of them looking\n "
                           "right at you as you walk through the forest.")


def forest_room4b():
    while True:
        slow_print("You come to a dead end in the path. The trees are\n "
                   "too tightly packed to squeeze through.")
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Back the way you came.")
        slow_print("2. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == str(1):
                slow_print("You turn around and go back.")
                slow_screen_clear()
                forest_room3b()
                return False
            elif choice == str(2):
                if adventurer.room4bitem is False:
                    slow_print("You notice something just past "
                               "a gap in the trees.")
                    slow_print("You reach through and grab it.")
                    slow_print("You found a Steel Sword!")
                    adventurer.inventory.append("Steel Sword")
                    adventurer.room4bitem = True
                    slow_screen_clear()
                else:
                    slow_print("You aren't able to see much thanks "
                               "to how dark it is due to the trees.")
                    slow_screen_clear()


def forest_room4c():
    while True:
        slow_print("The trees are growing much more closely together here, \n"
                   "forcing you to squeeze through or turn around.")
        slow_print("What will you do?\n")
        slow_print("1. Through the trees.")
        slow_print("2. Turn around.")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You squeeze yourself through "
                           "a gap in the trees.")
                slow_screen_clear()
                forest_room5c()
                return False
            elif choice == str(2):
                slow_print("You turn around and go back.")
                slow_screen_clear()
                forest_room3c()
                return False
            elif choice == str(3):
                if "Missing Necklace" in adventurer.quests:
                    slow_print("You notice something shining in a hole "
                               "in one of the tree trunks. \nReaching "
                               "inside you grab hold of an old necklace.")
                    adventurer.keyitems.append("Missing Necklace")
                    slow_screen_clear()
                else:
                    slow_print("It's too difficult to take notice of anything.")
                    slow_screen_clear()


def forest_room5a():

    while True:
        slow_print("You step into an empty clearing.\n"
                   "A breath of fresh air after the recent "
                   "squeeze through\nthose tight trees.")
        slow_print("What will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go East.")
        slow_print("3. Go West.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room6a()
                return False
            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room5c()
                return False
            elif choice == str(3):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room5b()
                return False
            elif choice == str(4):
                slow_print("You notice a small rabbit hopping "
                           "towards the western path.")
                slow_print("You hear a loud noise to the north.\n"
                           "Best to be prepared before you proceed.")
                slow_screen_clear()


def forest_room5b():
    slow_print("The air seems to glow as you step into a small clearing.\n"
               "It takes a moment but you realise that glow is actually\n"
               "dust sprinkling from a fairy's wings as it hovers above\n"
               "a small pool of water.")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Go Back.")
        slow_print("2. Try to speak to the fairy.")
        slow_print("3. Try to catch the fairy.")
        slow_print("4. Drink from the pool.")
        slow_print("5. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4) \
              and choice != str(5):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, 4, or 5.\n")
        else:
            if choice == str(1):
                slow_print("You turn around and leave the spring behind.")
                slow_screen_clear()
                forest_room5a()
                return False
            elif choice == str(2):
                slow_print("If she is capable of understanding you "
                           "or replying isn't clear.\n "
                           "Either way she gives no response.")
                slow_screen_clear()
            elif choice == str(3):
                slow_print("As you reach to try and grab the small fairy "
                           "a rush of dust suddenly\nflies into your face.\n"
                           "You wipe your eyes and when you can see again \n"
                           "you realise you are no longer at the fairy's pool...")
                slow_screen_clear()
                forest_room3b()
            if choice == str(4):
                slow_print("The fairy regards you curiously as you kneel down and\n"
                           "drink from the pool, but does nothing else.\n"
                           "The water instantly restores your vitality.")
                adventurer.recover_health(100)
                slow_print("The water has fully healed you!")
                slow_screen_clear()
            elif choice == str(5):
                slow_print("You look at the fairy. She is perhaps no\n"
                           "bigger than a hummingbird and is content to\n"
                           "simply watch you as you watch her.")


def forest_room5c():

    random_battle(random_enemy("Forest"), 3)

    while True:
        slow_print("You step into a tiny clearing, \n"
                   "surrounded on all side by densely packed trees.")
        slow_print("What will you do?\n")
        slow_print("1. Go North") # 6c
        slow_print("2. Go West.") # 5a
        slow_print("3. Go South.") # 4c
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room6c()
                return False
            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room5a()
                return False
            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room4c()
                return False
            elif choice == str(4):
                slow_print("You notice a path through the trees to the north,\n "
                           "with some sounds of laughter echoing through.")


def forest_room6a():
    slow_print("As you move through the trees you here an "
               "indescribable noise.\n Like something "
               "scracthing the very thoughts in your mind.")
    slow_print("A shadow bursts forth from between the trees!")
    spider = Enemy("Giant Spider", 50, 25, 10, 10, 150)
    battle_event(adventurer, spider)

    slow_print("With the spider defeated you press onward"
               "past its twitching corpse.\n"
               "Delaying here would only be dangerous.\n"
               "A nest is likely nearby and you aren't "
               "equipped to deal with it.")
    slow_screen_clear()
    forest_room7()

def forest_room6c():
    if adventurer.forest_6c_camp is False:
        slow_print("You step out of the trees and into a clearing where\n"
                   "some bandits have set up a camp!")
        bandit_camp = Enemy("Bandits", 50, 25, 10, 10, 100)
        battle_event(adventurer, bandit_camp)
        adventurer.forest_6c_camp = True
        if "Clear Bandit Camp" in adventurer.quests:
            slow_print("You have cleared the bandit camp!\n"
                       "Report your success in town!")
            adventurer.keyitems.append("Bandit Camp Cleared")
    
    else:
        slow_print("The camp is now silent, "
                   "save for the crackling of the dying fire.")

    while True:
        slow_print("You are standing at the center of the old bandit camp.")
        slow_print("What will you do?\n")
        slow_print("1. Go Back.")
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception
        except Exception:
            print("Please enter only 1, or 2.\n")
        else:
            if choice == 1:
                slow_print("You go back the way you came.")
                slow_screen_clear()
                forest_room5c()
                return False
            elif choice == 2:
                if "Missing Person" in adventurer.quests:
                    slow_print("As you look around you notice a "
                               "bundle of\nrags piled up with "
                               "some rope.\nTaking a closer look "
                               "you realise it is a person!\n"
                               "You cut them free, and give "
                               "them some supplies and "
                               "directions.\nThey are thankful "
                               "for the help and quickly run "
                               "from the forest back to town.")
                else:
                    slow_print("You notice some discarded rags.\n"
                               "You look through the bandit "
                               "supplies but find nothing of value.")


def forest_room7():
    while True:
        slow_print("The trees don't grow as tightly together here,\n"
                   "allowing you to rest in a small clearing as "
                   "you sit on a fallen log.")
        slow_print("What will you do?\n")
        slow_print("1. Leave")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1 or 2.\n")
        else:
            if choice == str(1):
                slow_print("You deprat from the forest,\n"
                           "heading toward the nearest town.")
                slow_screen_clear()
                town()
                return False
            elif choice == str(2):
                slow_print("The forest is eerily quiet here.\n"
                           "Perhaps the giant spiders had hunted "
                           "or scared all the other critters away.")
                slow_screen_clear()


def main():
    """
    Runs the primary functions for the game.
    """
    # splash_screen()
    shop()


main()
