# https://www.geeksforgeeks.org/clear-screen-python/
import os

# imported to create a character by character print function
from sys import stdout
from time import sleep

# imported for battle functionality
import random

# importing other scripts
from game_slow_functions import *
from game_intro import *
from game_characters import *


def main():
    """
    Runs the primary functions for the game.
    """
    splash_screen()


main()
