# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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

def splash_screen():
    """
    A function to display the splash screen to start, display rules, and end the game based on player input.
    """
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

def rules():
    """
    A function to display rules to the player.
    """
    print("In Averland Adventures you take on the role of a new adventurer.")
    print("It will be your job to fulfill quests for the townsfolk.")
    print("Slaying monsters, rescuing the innocent, recovering lost treasures.")
    print("The game will be played entirely using the number keys. (1,2,3, etc.)")
    print("Simply follow the on screen prompts to decide your next action.")
    print("Best of luck on your quests, brace Adventurer!")
    go_back = input("To return to the main menu, press 1:\n")
    if(go_back == str(1)):
        splash_screen()

def exit_game():
    """
    A function to end the game.
    """
    print("You will be missed, brave adventurer.")
    print("Perhaps we shall see you again, another time.")
    print("Farewell.")


def game_intro():
    """
    A function to begin the game.
    """
    print("Welcome to the kingdom of Averland, brave adventurer.\n")
    your_name = input("What is your name?")
    adventurer = Character(your_name, 100, 10, 10, 5)
    print(f"You are {adventurer.name}! You are a brave soul with {adventurer.health} points of health.\n")
    print(f"{adventurer.attack} attack, {adventurer.defence} defence, and {adventurer.speed} speed.\n")
    print(f"Prepare to embark on a thrilling adventure, in pursuit of fame and fortune, brave {adventurer.name}!\n")

def main():
    """
    Runs the primary functions for the game.
    """
    splash_screen()

main()