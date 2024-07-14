# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#https://www.geeksforgeeks.org/clear-screen-python/
import os
#imported to create a character by character print function
from sys import stdout
from time import sleep

#https://stackoverflow.com/questions/75486619/how-to-print-one-character-at-a-time-but-maintain-print-function-python
def slow_print(text, delay=0.025):
    """
    A function to print out lines character by character rather than having it presented immediately
    """
    if text: #checking for text content in the provided string
        for c in text:
            print(c, end='', flush=True)
            sleep(delay)
        if text[-1] != '\n':
            print()

"""
CHARACTER CLASSES AND METHODS
"""

#move to characters.py to define protag, enemies, etc in one file.
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
        damage_taken = self.attack - other_char.defence
        other_char.health -= damage_taken

class Player(Character):
    """
    Creates an Instance of a Player Character Class.
    """

    def __init__(self, name, health, attack, defence, speed, gold, inventory, quests):
        super().__init__(name, health, attack, defence, speed)
        self.gold = gold
        self.inventory = inventory
        self.quests = quests

class Enemy(Character):
    """
    Creates an Instance of an Enemy Character Class.
    """

    def __init__(self, name, health, attack, defence, speed):
        super().__init__(name, health, attack, defence, speed)

adventurer = Player("", 0, 0, 0, 0, 1000, ["Old Sword", "New Sword", "Steel Sword", "Potion", "Potion", "Potion", "Potion", "Potion"], [])

"""
INTRO FUNCTIONS
"""

#move to intro.py
def splash_screen():
    """
    A function to display the splash screen to start, display rules, and end the game based on player input.
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
            choice = input()
            if(choice != str(1) and choice != str(2)
                and choice != str(3)):
                raise Exception
        
        except Exception:
            print("Please enter only 1, 2 or 3.\n")
        
        else:
            if(choice == str(1)):
                game_intro()

            elif(choice == str(2)):
                rules()

            elif(choice == str(3)):
                exit_game()

#move to intro.py
def rules():
    """
    A function to display rules to the player.
    """
    #https://www.geeksforgeeks.org/clear-screen-python/
    #clearing screen before presenting new lines
    os.system('clear')
    slow_print("In Averland Adventures you take on the role of a new adventurer.")
    slow_print("It will be your job to fulfill quests for the townsfolk.")
    slow_print("Slaying monsters, rescuing the innocent, recovering lost treasures.")
    slow_print("The game will be played entirely using the number keys. (1,2,3, etc.)")
    slow_print("Simply follow the on screen prompts to decide your next action.")
    slow_print("Best of luck on your quests, brave Adventurer!")
    slow_print("\nTo return to the main menu, press 1:\n")
    while True:
        go_back = input()
        try:
            if(go_back != str(1)):
                raise Exception
        except Exception:
            print("Please press 1.\n")
        else:
            if(go_back == str(1)):
                splash_screen()

#move to intro.py
def exit_game():
    """
    A function to end the game.
    """
    os.system('clear')
    slow_print("You will be missed, brave adventurer.")
    slow_print("Perhaps we shall see you again, another time.")
    slow_print("Farewell.")

#move to intro.py
def game_intro():
    """
    A function to begin the game.
    """
    os.system('clear')
    slow_print("Welcome to the kingdom of Averland, brave adventurer.")
    while True:
        slow_print("What is your name?")
        print("(Use alphabetic characters only and use less than 20 characters)")
        your_name = input()
        try:
            if(your_name.isalpha() is False):
                raise Exception
            elif(len(your_name) > 20):
                raise Exception
        except Exception:
            print("Please keep your name under 20 characters and only use alphabetic characters.\n")
        else:
            adventurer = Player(your_name, 100, 10, 10, 5, 10, ["Old Sword", "Old Shield"], ["Empty"])
            slow_print(f"You are {adventurer.name}! You are a brave soul with {adventurer.health} points of health.")
            slow_print(f"{adventurer.attack} attack, {adventurer.defence} defence, {adventurer.speed} speed and {adventurer.gold} gold pieces.")
            slow_print(f"You have {adventurer.inventory} in your inventory.")
            slow_print(f"Your quest log is {adventurer.quests}... for now.")
            slow_print(f"Prepare to embark on a thrilling adventure, in pursuit of fame and fortune, brave {adventurer.name}!\n")
            slow_print("...", 0.25)
            slow_print("..", 0.25)
            slow_print(".", 0.25)
            town()
            return False

"""
HUBWORLD FUNCTIONS
"""

#move to hubworld.py
def town():
    """
    A function to hold the Town the player will return to after completing each adventure.
    """
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
            if(choice != str(1) and choice != str(2)
                and choice != str(3) and choice != str(4)):
                raise Exception
        except:
            print("Please enter only 1, 2, 3 or 4.\n")
        else:
            if(choice == str(1)):
                shop()
                return False

            elif(choice == str(2)):
                find_a_quest()
                return False

            elif(choice == str(3)):
                begin_adventure()
                return False

            elif(choice == str(4)):
                os.system('clear')
                slow_print(f"Rest now, brave {adventurer.name}.")
                slow_print("Perhaps we shall see you again, another time.")
                slow_print("Farewell.")
                return False

#move to hubworld.py
def shop():
    """
    A function to hold the Shop the player can spend their gold or sell their items at.
    """
    #methods specific to shopping
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
                if(choice != str(1) and choice != str(2)
                    and choice != str(3) and choice != str(4)):
                    raise Exception
            except:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if(choice == str(1)):
                    while True:
                        print("Available weapons for sale:")
                        print("1. Iron Sword: +2 Attack when equipped. 50 gold.")
                        print("2. Steel Sword: +4 Attack when equipped. 150 gold.")
                        print("3. Silver Sword: +6 Attack when equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if(choice != str(1) and choice != str(2)
                                and choice != str(3) and choice != str(4)):
                                raise Exception
                        except:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if(choice == str(1)):
                                if(adventurer.gold <= 50):
                                    print("You cannot afford this item.")
                                elif("Iron Sword" in adventurer.inventory):
                                    print("You already own an Iron Sword")
                                else:
                                    print("You have added an Iron Sword to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Iron Sword")
                            elif(choice == str(2)):
                                if(adventurer.gold <= 150):
                                    print("You cannot afford this item.")
                                elif("Steel Sword" in adventurer.inventory):
                                    print("You already own a Steel Sword")
                                else:
                                    print("You have added a Steel Sword to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Steel Sword")
                            elif(choice == str(3)):
                                if(adventurer.gold <= 300):
                                    print("You cannot afford this item.")
                                elif("Silver Sword" in adventurer.inventory):
                                    print("You already own a Silver Sword")
                                else:
                                    print("You have added a Silver Sword to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Silver Sword")
                            elif(choice == str(4)):
                                shop()
                                return False

                elif(choice == str(2)):
                    while True:
                        print("Available armor for sale:")
                        print("1. Iron Armor: +2 Defence when equipped. 50 gold.")
                        print("2. Steel Armor: +4 Defence when equipped. 150 gold.")
                        print("3. Silver Armor: +6 Defence when equipped. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if(choice != str(1) and choice != str(2)
                                and choice != str(3) and choice != str(4)):
                                raise Exception
                        except:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if(choice == str(1)):
                                if(adventurer.gold <= 50):
                                    print("You cannot afford this item.")
                                elif("Iron Armor" in adventurer.inventory):
                                    print("You already own Iron Armor")
                                else:
                                    print("You have added Iron Armor to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Iron Armor")
                            elif(choice == str(2)):
                                if(adventurer.gold <= 150):
                                    print("You cannot afford this item.")
                                elif("Steel Armor" in adventurer.inventory):
                                    print("You already own Steel Armor")
                                else:
                                    print("You have added Steel Armor to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Steel Armor")
                            elif(choice == str(3)):
                                if(adventurer.gold <= 300):
                                    print("You cannot afford this item.")
                                elif("Silver Armor" in adventurer.inventory):
                                    print("You already own a Silver Armor")
                                else:
                                    print("You have added Silver Armor to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Silver Armor")
                            elif(choice == str(4)):
                                shop()
                                return False
                    

                elif(choice == str(3)):
                    while True:
                        print("Available items for sale:")
                        print("1. Potion. Restore 25 Health. 50 gold.")
                        print("2. Large Potion. Restore 50 Health. 150 gold.")
                        print("3. Max Potion: Fully restore Health. 300 gold.")
                        print("4. Check other options.")
                        choice = input()
                        try:
                            if(choice != str(1) and choice != str(2)
                                and choice != str(3) and choice != str(4)):
                                raise Exception
                        except:
                            print("Please enter only 1, 2, 3, or 4.\n")
                        else:
                            if(choice == str(1)):
                                if(adventurer.gold <= 50):
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Potion to your inventory.")
                                    adventurer.inventory.append("Potion")
                            elif(choice == str(2)):
                                if(adventurer.gold <= 150):
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Large Potion to your inventory.")
                                    adventurer.inventory.append("Large Potion")
                            elif(choice == str(3)):
                                if(adventurer.gold <= 300):
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Max Potion to your inventory. Remember to equip it.")
                                    adventurer.inventory.append("Max Potion")
                            elif(choice == str(4)):
                                shop()
                                return False

                elif(choice == str(4)):
                    find_a_quest()
                    return False

    def sell():
        os.system('clear')
        slow_print("You open your bag to see what you could sell to the shopkeep.\n")
        #https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3
        while True:
            available_items = 0
            for number, items_owned in enumerate(adventurer.inventory):
                print(number+1, items_owned)
                available_items+=1
            print("What would you like to sell? Press 0 to return to the shop.")
            choice = int(input())
            try:
                if(choice > available_items and choice.alpha() is False):
                    raise Exception
            except Exception:
                print("Please only enter the numbers on screen, or 0 to return to the shop.")
            else:
                if(choice == 0):
                    shop()
                    return False
                elif(choice <= available_items and choice > 0):
                    if(adventurer.inventory[choice-1] == "Iron Sword" or adventurer.inventory[choice-1] == "Iron Armor"
                        or adventurer.inventory[choice-1] == "Potion"):
                        adventurer.gold += 25
                        print(f"You got 25 gold from selling your {adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)
                    elif(adventurer.inventory[choice-1] == "Steel Sword" or adventurer.inventory[choice-1] == "Steel Armor"
                        or adventurer.inventory[choice-1] == "Large Potion"):
                        adventurer.gold += 50
                        print(f"You got 50 gold from selling your {adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)
                    elif(adventurer.inventory[choice-1] == "Silver Sword" or adventurer.inventory[choice-1] == "Silver Armor"
                        or adventurer.inventory[choice-1] == "Max Potion"):
                        adventurer.gold += 150
                        print(f"You got 150 gold from selling your {adventurer.inventory[choice-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(choice-1)
                    else:
                        adventurer.gold += 10
                        print(f"You got 10 gold from selling your {adventurer.inventory[choice-1]}.")
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
        choice = input()
        try:
            if(choice != str(1) and choice != str(2)
                and choice != str(3)):
                raise Exception
        except:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if(choice == str(1)):
                buy()
                return False

            elif(choice == str(2)):
                sell()
                return False

            elif(choice == str(3)):
                leave_shop()
                return False

#move to hubworld.py
def find_a_quest():
    """
    A function to hold the tavern where the player can find new quests.
    """

    #methods specific to the tavern for quests
    def quest_board():
        os.system('clear')
        slow_print("You check the quest board for official quests from the town guild.\n")
        while True:
            print("Currently available quests:")
            print("1. Slay 5 slimes on the Merchant Road")
            print("2. Defend a caravan on the Merchant Road")
            print("3. Clear out a bandit camp in the Forest")
            print("4. Leave the quest board")
            print("What quest will you accept?\n")
            choice = input()
            try:
                if(choice != str(1) and choice != str(2)
                    and choice != str(3) and choice != str(4)):
                    raise Exception
            except:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if(choice == str(1)):
                    if("Slay Slimes" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to defeat Slimes.")
                        adventurer.quests.append("Slay Slimes")

                elif(choice == str(2)):
                    if("Defend Caravan" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to defend a merchant caravan.")
                        adventurer.quests.append("Defend Caravan")

                elif(choice == str(3)):
                    if("Clear Bandit Camp" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to clear out a bandit camp.")
                        adventurer.quests.append("Clear Bandit Camp")
                elif(choice == str(4)):
                    find_a_quest()
                    return False

    def ask_a_local():
        os.system('clear')
        slow_print("You ask a local and they tell you about some jobs you could do.\n")
        while True:
            print("Currently available quests:")
            print("1. Find lost necklace on the Merchant Road")
            print("2. Person missing in the forest")
            print("3. Bandit kidnapping")
            print("4. Leave the locals")
            print("Will you offer help with any of their jobs?\n")
            choice = input()
            try:
                if(choice != str(1) and choice != str(2)
                    and choice != str(3) and choice != str(4)):
                    raise Exception
            except:
                print("Please enter only 1, 2, 3, or 4.\n")
            else:
                if(choice == str(1)):
                    if("Missing Necklace" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have offered to help find the necklace.")
                        adventurer.quests.append("Missing Necklace")

                elif(choice == str(2)):
                    if("Missing Person" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help find the missing person.")
                        adventurer.quests.append("Missing Person")

                elif(choice == str(3)):
                    if("Bandit Kidnapping" in adventurer.quests):
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help rescue the kidnapped person.")
                        adventurer.quests.append("Bandit Kidnapping")
                elif(choice == str(4)):
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
            if(choice != str(1) and choice != str(2)
                and choice != str(3)):
                raise Exception
        except:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if(choice == str(1)):
                quest_board()
                return False

            elif(choice == str(2)):
                ask_a_local()
                return False

            elif(choice == str(3)):
                leave_tavern()
                return False

#move to hubworld.py
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
            if(choice != 1 and choice != 2
                and choice != 3):
                raise Exception
        except:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if(choice == 1):
                os.system('clear')
                slow_print("You travel the merchant's road.\n")
                road_start()
                return False

            elif(choice == 2):
                os.system('clear')
                slow_print("You depart towards the forest\n")

            elif(choice == 3):
                os.system('clear')
                slow_print("You turn around and go back to the town square.\n")
                town()
                return False


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
            if(choice != 1 and choice != 2
                and choice != 3):
                raise Exception
        except:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if(choice == 1):
                road_1()
                return False
            elif(choice == 2):
                print("flavour text for looking")
            elif(choice == 3):
                print("You decide you are unprepared and return to town.")
                delay(1.5)
                town()
                return False

def road_1():
    found_gold_road_1 = False
    print("flavour text")
    while True:
        os.system('clear')
        slow_print("What will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if(choice != 1 and choice != 2
                and choice != 3):
                raise Exception
        except:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if(choice == 1):
                print("You continue down the road.")
                road_2()
                return False
            elif(choice == 2):
                if(found_gold_road_1 is not True):
                    print("flavour text for looking. you found gold!")
                    adventurer.gold += 10
                    found_gold_road_1 = True
                    sleep(1.5)
                else:
                    print("There is nothing else of interest.")
                    sleep(1.5)

def road_2():
    #bandit battle, leads to road 3
    pass

def road_3():
    #empty, can notice the side road (3a) or go to 4
    pass

    def road_3a():
        pass
        #empty, look to find tracks to go to 3b

    def road_3b():
        pass
        #battle before 3c

    def road3c():
        pass
        #large battle

def road_4():
    #notice signs of a fight, 4a
    #proceed to 5

    def road_4a():
        #fight
        pass

    def road_4b():
        #fight
        pass

def road_5():
    #fight
    pass

def road_6():
    #fight?
    pass

def road_7():
    #town ahead
    pass


"""
FOREST EVENTS
"""

def forest_start():
    pass
    #leads to forest1a

def forest_room1a():
    pass
    #forest1b or 2a

def forest_room1b():
    pass
    #forest 1a or 2b

def forest_room1c():
    pass
    #forest 2c

def forest_room2a():
    pass
    # forest 1a, 2b, 2c

def forest_room2b():
    pass
    # forest 2a or 3b

def forest_room2c():
    pass
    #forest 2a or 1c

def forest_room3a():
    pass
    #forst 3b or 3c

def forest_room3b():
    pass
    #forest 4b or 3a

def forest_room3c():
    pass
    #forest 4c

def forest_room4b():
    pass
    #forest 3b

def forest_room4c():
    pass
    #forest 5c

def forest_room5a():
    pass
    #forest 5c, 5b, or 6a

def forest_room5b():
    pass
    #forest 5a

def forest_room5c():
    pass
    #forest 5a or 6c

def forest_room6a():
    pass
    #forest 7

def forest_room6c():
    pass
    #forest 5c

def forest_room7():
    pass
    #end

def main():
    """
    Runs the primary functions for the game.
    """
    adventurer = Player("Chris", 100, 10, 10, 5, 10, ["Old Sword", "Old Shield"], [])
    #splash_screen()
    begin_adventure()

main()