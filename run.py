# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#https://www.geeksforgeeks.org/clear-screen-python/
import os
#imported to create a character by character print function
from sys import stdout
from time import sleep

#move to characters.py to define protag, enemies, etc in one file.
class Character:
    """
    Creates an Instance of a Character Class.
    """

    def __init__(self, name, health, attack, defence, speed, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.gold = gold

#move to intro.py
def splash_screen():
    """
    A function to display the splash screen to start, display rules, and end the game based on player input.
    """
    os.system('clear')
    print("Averland Adventures\n")
    print("A text based choose your own adventure RPG game.")
    print("1. Start Game")
    print("2. Read Rules")
    print("3. Exit Game")
    choice = input("What would you like to do?\n")
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
    print("In Averland Adventures you take on the role of a new adventurer.")
    print("It will be your job to fulfill quests for the townsfolk.")
    print("Slaying monsters, rescuing the innocent, recovering lost treasures.")
    print("The game will be played entirely using the number keys. (1,2,3, etc.)")
    print("Simply follow the on screen prompts to decide your next action.")
    print("Best of luck on your quests, brace Adventurer!")
    go_back = input("To return to the main menu, press 1:\n")
    if(go_back == str(1)):
        splash_screen()

#move to intro.py
def exit_game():
    """
    A function to end the game.
    """
    os.system('clear')
    print("You will be missed, brave adventurer.")
    print("Perhaps we shall see you again, another time.")
    print("Farewell.")

#move to intro.py
def game_intro():
    """
    A function to begin the game.
    """
    os.system('clear')
    print("Welcome to the kingdom of Averland, brave adventurer.")
    your_name = input("What is your name?\n")
    adventurer = Character(your_name, 100, 10, 10, 5, 10)
    print(f"You are {adventurer.name}! You are a brave soul with {adventurer.health} points of health.")
    print(f"{adventurer.attack} attack, {adventurer.defence} defence, {adventurer.speed} speed and {adventurer.gold} gold pieces.")
    print(f"Prepare to embark on a thrilling adventure, in pursuit of fame and fortune, brave {adventurer.name}!\n")
    town()

#move to hubworld.py
def town():
    """
    A function to hold the Town the player will return to after completing each adventure.
    """
    sleep(3)
    os.system('clear')
    print("PLACEHOLDER TEXT")
    print("You are in town.")
    print("1. Shop.")
    print("2. Accept a quest.")
    print("3. Depart on an adventure.")
    print("4. Rest and end your adventures.")
    choice = input("What would you like to do?\n")
    if(choice == str(1)):
        shop()

    elif(choice == str(2)):
        find_a_quest()

    elif(choice == str(3)):
        begin_adventure()

    elif(choice == str(4)):
        os.system('clear')
        print("Rest now, brave adventurer.")
        print("Perhaps we shall see you again, another time.")
        print("Farewell.")

    else:
        print("error")

#move to hubworld.py
def shop():
    """
    A function to hold the Shop the player can spend their gold or sell their items at.
    """
    os.system('clear')
    print("PLACEHOLDER TEXT")
    print("You are in the shop.")
    print("1. Buy.")
    print("2. Sell.")
    print("3. Leave.")

    def buy():
        os.system('clear')
        print("Buy things.\n")
        shop()

    def sell():
        os.system('clear')
        print("Sell things.\n")
        shop()

    def leave_shop():
        os.system('clear')
        print("You leave.\n")
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
    print("You are in the tavern.")
    print("1. Check the Quest Board.")
    print("2. Ask a local for work.")
    print("3. Leave.")

    def quest_board():
        os.system('clear')
        print("You check the board and accept X.\n")
        find_a_quest()

    def ask_a_local():
        os.system('clear')
        print("You ask a local and they tell you X.\n")
        find_a_quest()

    def leave_tavern():
        os.system('clear')
        print("You leave.\n")
        town()

    choice = input("What would you like to do?\n")
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
    print("You set out from town.")
    print("1. Merchant Road.")
    print("2. Forest.")
    print("3. Stay in Town.")

    choice = input("What is your destination?\n")
    if(choice == str(1)):
        os.system('clear')
        print("You depart towards the forest.\n")

    elif(choice == str(2)):
        os.system('clear')
        print("You travel the merchant's road.\n")

    elif(choice == str(3)):
        os.system('clear')
        print("You turn around and go back to the town square.\n")
        town()

    else:
        print("error")

def main():
    """
    Runs the primary functions for the game.
    """
    splash_screen()

main()