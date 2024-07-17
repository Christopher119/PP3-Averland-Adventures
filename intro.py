# https://www.geeksforgeeks.org/clear-screen-python/
import os
# imported to create a character by character print function
from sys import stdout
from time import sleep

from slow_functions import *

def splash_screen():
    """
    A function to display the splash screen to start, display rules,
    and end the game based on player input.
    """
    os.system('clear')
    while True:
        slow_print("Averland Adventures\n")
        slow_print("A text based choose your own adventure RPG game.")
        slow_print("What would you like to do?\n")
        slow_print("1. Start Game")
        slow_print("2. Read Rules")
        slow_print("3. Exit Game")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2 or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                game_intro()

            elif choice == str(2):
                rules()

            elif choice == str(3):
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
        go_back = input()
        try:
            if go_back != str(1):
                raise Exception
        except Exception:
            print("Please press 1.\n")
            slow_screen_clear()
        else:
            if go_back == str(1):
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
            slow_screen_clear()
        else:
            adventurer = Player(your_name, 100, 10, 10, 5, 10,
                                ["Old Sword", "Old Shield"], ["Empty"])
            slow_print(f"You are {adventurer.name}! You are a brave soul "
                       f"with {adventurer.health} points of health.")
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
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception
        except Exception:
            print("Please enter only 1 or 2.\n")
        else:
            if choice == str(1):
                slow_print("May your efforts bear more fruit "
                           "this time, adventurer.\n")
                game_intro()
                return False

            elif choice == str(2):
                slow_print("Perhaps we shall meet again in another life.\n")
                sleep(3)
                quit()
                return False