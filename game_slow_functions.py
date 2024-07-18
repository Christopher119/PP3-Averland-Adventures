# https://www.geeksforgeeks.org/clear-screen-python/
import os
# imported to create a character by character print function
from sys import stdout
from time import sleep


def slow_print(text, delay=0.025):
    """
    A function to print out lines character by character
    rather than having it presented immediately
    """
    # https://stackoverflow.com/questions/75486619/how-to-print-one-character-at-a-time-but-maintain-print-function-python
    # checking for text content in the provided string
    if text:
        # for every character in the provided string
        for c in text:
            # print the character, flush the internal buffer
            print(c, end='', flush=True)
            # delay the next print by defined amount
            sleep(delay)

        if text[-1] != '\n':
            print()


def slow_screen_clear():
    """
    This function pauses the game for 2 seconds before clearing the terminal.
    A simple method to pause and allow a player to read what was printed before
    the terminal clears itself to progress to the next function.
    """
    sleep(2)
    os.system('clear')
