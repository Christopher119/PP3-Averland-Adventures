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

#move to intro.py
def splash_screen():
    """
    A function to display the splash screen to start, display rules, and end the game based on player input.
    """
    os.system('clear')
    slow_print("Averland Adventures\n")
    slow_print("A text based choose your own adventure RPG game.")
    slow_print("What would you like to do?\n")
    slow_print("1. Start Game")
    slow_print("2. Read Rules")
    slow_print("3. Exit Game")
    choice = input()
    if(choice == str(1)):
        game_intro()

    elif(choice == str(2)):
        rules()

    elif(choice == str(3)):
        exit_game()

    else:
        print("error")

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
    slow_print("Best of luck on your quests, brace Adventurer!")
    slow_print("\nTo return to the main menu, press 1:\n")
    go_back = input()
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
    slow_print("What is your name?\n")
    your_name = input()
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

#move to hubworld.py
def town():
    """
    A function to hold the Town the player will return to after completing each adventure.
    """
    os.system('clear')
    print("PLACEHOLDER TEXT")
    slow_print("You are in town.")
    slow_print("What would you like to do?\n")
    slow_print("1. Shop.")
    slow_print("2. Accept a quest.")
    slow_print("3. Depart on an adventure.")
    slow_print("4. Rest and end your adventures.")
    choice = input()
    if(choice == str(1)):
        shop()

    elif(choice == str(2)):
        find_a_quest()

    elif(choice == str(3)):
        begin_adventure()

    elif(choice == str(4)):
        os.system('clear')
        slow_print("Rest now, brave adventurer.")
        slow_print("Perhaps we shall see you again, another time.")
        slow_print("Farewell.")

    else:
        print("error")

#move to hubworld.py
def shop():
    """
    A function to hold the Shop the player can spend their gold or sell their items at.
    """
    os.system('clear')
    print("PLACEHOLDER TEXT")
    slow_print("You are in the shop.")
    slow_print("What would you like to do?\n")
    slow_print("1. Buy.")
    slow_print("2. Sell.")
    slow_print("3. Leave.")

    def buy():
        os.system('clear')
        slow_print("Buy things.\n")
        shop()

    def sell():
        os.system('clear')
        slow_print("Sell things.\n")
        shop()

    def leave_shop():
        os.system('clear')
        slow_print("You leave.\n")
        town()

    choice = input("What would you like to do?\n")
    if(choice == str(1)):
        buy()

    elif(choice == str(2)):
        sell()

    elif(choice == str(3)):
        leave_shop()

    else:
        print("error")

#move to hubworld.py
def find_a_quest():
    os.system('clear')
    print("PLACEHOLDER TEXT")
    slow_print("You are in the tavern.")
    slow_print("What would you like to do?\n")
    slow_print("1. Check the Quest Board.")
    slow_print("2. Ask a local for work.")
    slow_print("3. Leave.")

    def quest_board():
        os.system('clear')
        slow_print("You check the board and accept X.\n")
        find_a_quest()

    def ask_a_local():
        os.system('clear')
        slow_print("You ask a local and they tell you X.\n")
        find_a_quest()

    def leave_tavern():
        os.system('clear')
        slow_print("You leave.\n")
        town()

    choice = input()
    if(choice == str(1)):
        quest_board()

    elif(choice == str(2)):
        ask_a_local()

    elif(choice == str(3)):
        leave_tavern()

    else:
        print("error")

#move to hubworld.py
def begin_adventure():
    os.system('clear')
    print("PLACEHOLDER TEXT")
    slow_print("You set out from town.")
    slow_print("What is your destination?\n")
    slow_print("1. Merchant Road.")
    slow_print("2. Forest.")
    slow_print("3. Stay in Town.")

    choice = input()
    if(choice == str(1)):
        os.system('clear')
        slow_print("You depart towards the forest.\n")

    elif(choice == str(2)):
        os.system('clear')
        slow_print("You travel the merchant's road.\n")

    elif(choice == str(3)):
        os.system('clear')
        slow_print("You turn around and go back to the town square.\n")
        town()

    else:
        print("error")

def main():
    """
    Runs the primary functions for the game.
    """
    splash_screen()

main()