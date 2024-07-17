# https://www.geeksforgeeks.org/clear-screen-python/
import os
# imported to create a character by character print function
from sys import stdout
from time import sleep

def slow_print(text, delay=0.025):
    """
    A function to print out lines character by character rather
    than having it presented immediately
    """
    # https://stackoverflow.com/questions/75486619/how-to-print-one-character-at-a-time-but-maintain-print-function-python
    if text:  # checking for text content in the provided string
        for c in text:
            print(c, end='', flush=True)
            sleep(delay)
        if text[-1] != '\n':
            print()


def slow_screen_clear():
    sleep(2)
    os.system('clear')