# Import necessary modules.
import pyfiglet
import random
import time
import sys
from time import sleep
from colorama import Fore, Style

# Code reference from https://stackoverflow.com/questions/20302331/typing-effect-in-python
def typewriter_print(text, speed=0.03):
    '''
    This function add the typewriter effect.
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def welcome_message():
    """
    This function showcase the welcome message,
    logo design, explain what the program is
    and lead to the get_user_name function.
    """
    print(
        Fore.CYAN
        + "===================================="
        + "==============================\n"
    )
    print(Style.RESET_ALL)
    print(pyfiglet.figlet_format("Password", font="larry3d"))
    print(pyfiglet.figlet_format("Creator", font="larry3d"))
    print(
        Fore.CYAN
        + "===================================="
        + "=============================="
    )
    print(Style.RESET_ALL)
    time.sleep(.5)
    typewriter_print("Welcome to the password creator!")
    typewriter_print(
        "Did you know it only takes seconds to hack "
        + "small passwords?"
    )
    typewriter_print(
        "We provide a secure password, all we need is that you "
        + "follow two steps and choose:"
    )
    typewriter_print("1 - Between 8 and 64 characters long.")
    typewriter_print(
        "2 - Letters only or mixed characters (letters/numbers/symbols)."
    )

welcome_message()