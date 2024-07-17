from slow_functions import *
from characters import *
from game_variables import *
from game_road import *
from game_forest import *

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
            slow_screen_clear()
        else:
            if choice == str(1):
                slow_print("You walk towards the local shop, "
                           "the bell\nabove the door jingling "
                           "as you enter.")
                slow_screen_clear()
                shop()
                return False

            elif choice == str(2):
                slow_print("You walk towards the tavern, "
                           "the hustle and bustle of the\n"
                           "patrons already audible before"
                           "you open the door.")
                slow_screen_clear()
                find_a_quest()
                return False

            elif choice == str(3):
                slow_print("You walk towards the town gates, "
                           "where guards\nand other adventurers "
                           "are gathered.")
                slow_screen_clear()
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
        while True:
            print("You approach the shopkeep and ask what they have for sale.")
            print("Shop selection:")
            print("1. Weapons")
            print("2. Armor")
            print("3. Items")
            print("4. Back to options")
            print("What would you like to do?\n")
            choice = input()
            try:
                if choice != str(1) and choice != str(2) \
                 and choice != str(3) and choice != str(4):
                    raise Exception
            except Exception:
                print("Please enter only 1, 2, 3, or 4.\n")
                slow_screen_clear()
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
                            slow_screen_clear()
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
                                slow_screen_clear()
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
                                slow_screen_clear()
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
                                slow_screen_clear()
                            elif choice == str(4):
                                os.system('clear')
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
                            slow_screen_clear()
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
                                slow_screen_clear()
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
                                slow_screen_clear()
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
                                slow_screen_clear()
                            elif choice == str(4):
                                os.system('clear')
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
                            slow_screen_clear()
                        else:
                            if choice == str(1):
                                if adventurer.gold <= 50:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Potion")
                                slow_screen_clear()
                            elif choice == str(2):
                                if adventurer.gold <= 150:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Large Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Large Potion")
                                slow_screen_clear()
                            elif choice == str(3):
                                if adventurer.gold <= 300:
                                    print("You cannot afford this item.")
                                else:
                                    print("You have added a Max Potion "
                                          "to your inventory.")
                                    adventurer.inventory.append("Max Potion")
                                slow_screen_clear()
                            elif choice == str(4):
                                os.system('clear')
                                shop()
                                return False

                elif choice == str(4):
                    shop()
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
                    if (adventurer.inventory[int(choice)-1]
                       == "Iron Sword"
                       or adventurer.inventory[int(choice)-1]
                       == "Iron Armor"
                       or adventurer.inventory[int(choice)-1]
                       == "Potion"):
                        adventurer.gold += 25
                        print("You got 25 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

                    elif (adventurer.inventory[int(choice)-1]
                          == "Steel Sword"
                          or adventurer.inventory[int(choice)-1]
                          == "Steel Armor"
                          or adventurer.inventory[int(choice)-1]
                          == "Large Potion"):
                        adventurer.gold += 50
                        print("You got 50 gold from selling your "
                              f"{adventurer.inventory[int(choice)-1]}.")
                        print(f"Current gold: {adventurer.gold}")
                        adventurer.inventory.pop(int(choice)-1)

                    elif (adventurer.inventory[int(choice)-1]
                            == "Silver Sword"
                          or adventurer.inventory[int(choice)-1]
                            == "Silver Armor"
                          or adventurer.inventory[int(choice)-1]
                            == "Max Potion"):
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
        slow_print("You leave the shop and return to the center of town.\n")
        slow_screen_clear()
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
            slow_screen_clear()
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
        while True:
            slow_print("You check the quest board for "
                       "official quests from the town guild.\n")
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
                slow_screen_clear()
            else:
                if choice == str(1):
                    if "Slay Slimes" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defeat Slimes.")
                        adventurer.quests.append("Slay Slimes")
                        slow_screen_clear()

                elif choice == str(2):
                    if "Defend Caravan" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "defend a merchant caravan.")
                        adventurer.quests.append("Defend Caravan")
                        slow_screen_clear()

                elif choice == str(3):
                    if "Clear Bandit Camp" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have accepted the quest to "
                              "clear out a bandit camp.")
                        adventurer.quests.append("Clear Bandit Camp")
                        slow_screen_clear()

                elif choice == str(4):
                    os.system('clear')
                    find_a_quest()
                    return False

    def ask_a_local():
        while True:
            slow_print("You ask a local and they tell you "
                       "about some jobs you could do.\n")
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
                slow_screen_clear()
            else:
                if choice == str(1):
                    if "Missing Necklace" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have offered to help find the necklace.")
                        adventurer.quests.append("Missing Necklace")
                    slow_screen_clear()

                elif choice == str(2):
                    if "Missing Person" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "find the missing person.")
                        adventurer.quests.append("Missing Person")
                    slow_screen_clear()

                elif choice == str(3):
                    if "Bandit Kidnapping" in adventurer.quests:
                        print("You have already accepted this quest.")
                    else:
                        print("You have agreed to help "
                              "rescue the kidnapped person.")
                        adventurer.quests.append("Bandit Kidnapping")
                    slow_screen_clear()

                elif choice == str(4):
                    find_a_quest()
                    return False

    def leave_tavern():
        slow_print("You leave the tavern and return to the center of town.\n")
        slow_screen_clear()
        town()

    while True:
        slow_print("You are in the tavern.")
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
            slow_screen_clear()
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
    while True:
        slow_print("You are at the town gates.")
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
            slow_screen_clear()
        else:
            if choice == str(1):
                slow_print("You travel the merchant's road.\n")
                slow_screen_clear()
                road_start()
                return False

            elif choice == str(2):
                slow_print("You depart towards the forest\n")
                slow_screen_clear()
                forest_start()
                return False

            elif choice == str(3):
                slow_print("You turn around and go back to the town square.\n")
                slow_screen_clear()
                town()
                return False