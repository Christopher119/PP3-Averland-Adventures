from game_slow_functions import *
from game_characters import *
from game_hubworld import town


def splash_screen():
    """
    A function to display the splash screen to start, display rules,
    and end the game based on player input.
    """
    os.system('clear')
    while True:
        slow_print("Averland Adventures\n")
        slow_print("A text based choose your own adventure RPG game.")
        slow_print("\nWhat would you like to do?\n")
        slow_print("1. Start Game")
        slow_print("2. Read Rules")
        slow_print("3. Exit Game")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            slow_print("Please enter only 1, 2 or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                game_intro()
                return False

            elif choice == str(2):
                rules()
                return False

            elif choice == str(3):
                exit_game()
                return False


def rules():
    """
    A function to display rules to the player.
    """
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
            slow_print("Please press 1.")
        else:
            if go_back == str(1):
                splash_screen()
                return False


def exit_game():
    """
    A function to end the game.
    """
    os.system('clear')
    slow_print("You will be missed, brave adventurer.")
    slow_print("Perhaps we shall see you again, another time.")
    slow_print("Farewell.")
    quit()


def game_intro():
    """
    A function to begin the game.
    """
    os.system('clear')
    slow_print("Welcome to the kingdom of Averland, brave adventurer.")
    while True:
        slow_print("What is your name?")
        slow_print("(Use alphabetic characters only "
                   "and use less than 20 characters)")
        your_name = input()
        try:
            if your_name.isalpha() is False:
                raise Exception
            elif len(your_name) > 20:
                raise Exception
        except Exception:
            slow_print("Please keep your name under 20 characters "
                       "and only use alphabetic characters.\n")
            slow_screen_clear()
        else:
            adventurer.update_values(Player(your_name, 100, 10, 10, 5, 1000,
                                     ["Potion"], [], "", ""))
            slow_print(f"You are {adventurer.name}! You are a brave soul "
                       f"with {adventurer.health} points of health.")
            slow_print(f"{adventurer.attack} attack, {adventurer.defence} "
                       f"defence, {adventurer.speed} speed and "
                       f"{adventurer.gold} gold pieces.")
            slow_print(f"You have a {adventurer.inventory[0]} "
                       "in your inventory.")
            slow_print(f"Your quest log is empty for now.")
            slow_print(f"Prepare to embark on a thrilling adventure,\n"
                       "in pursuit of fame and fortune, "
                       f"brave {adventurer.name}!\n")
            slow_print("...", 0.25)
            slow_print("..", 0.25)
            slow_print(".", 0.25)
            town()
            return False
