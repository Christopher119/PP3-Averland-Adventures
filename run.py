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


def game_intro():
    print("Welcome to the kingdom of Averland, brave adventurer.\n")
    your_name = input("Please tell us your name:\n")
    adventurer = Character(your_name, 100, 10, 10, 5)
    print(f"You are {adventurer.name}! You are a brave soul with {adventurer.health} points of health.\n")
    print(f"{adventurer.attack} attack, {adventurer.defence} defence, and {adventurer.speed} speed.\n")
    print(f"Prepare to embark on a thrilling adventure, in pursuit of fame and fortune, brave {adventurer.name}!\n")

def main():
    """
    Runs the primary functions for the game.
    """
    game_intro()

main()