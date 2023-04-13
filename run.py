# Import necessary modules.
import pyfiglet
import random
import time
import sys
import os
from time import sleep
from colorama import Fore, Style

# Code to create the typewriter effect, credit:
# https://stackoverflow.com/questions/20302331/typing-effect-in-python
def typewriter_print(text, speed=0.03):
    """
    This function add the typewriter effect.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def clear_terminal():
    """
    This function clear the terminal.
    """
    os.system("clear")

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
        + "follow two steps:"
    )
    typewriter_print("1 - Choose between 8 and 64 characters long.")
    typewriter_print(
        "2 - Choose letters only or mixed characters (letters/numbers/symbols)."
    )

    while True:
        name = input("First things first, enter your name? \n").strip()
        if name == "":
            print(Fore.LIGHTRED_EX + "\nTry again, name cannot be blank.")
            print(Style.RESET_ALL)
        elif len(name) < 3:
            print(Fore.LIGHTRED_EX + "\nTry again, a minimum of 3 characters.")
            print(Style.RESET_ALL)
        elif len(name) > 16:
            print(Fore.LIGHTRED_EX + "\nTry again, a maximum of 16 characters.")
            print(Style.RESET_ALL)
        elif name.isdigit():
            print(Fore.LIGHTRED_EX + "\nTry again, letters only.")
            print(Style.RESET_ALL)
        else:
            typewriter_print(f"\nHi {name}, let's make your unique password!")
            time.sleep(2)
            clear_terminal()
            break

def get_length():
    """This function takes the password length chosen
    by the user. The user's input will be stored as
    an integer and needs to be a number between
    8 and 64, otherwise will raise an exception.
    """
    typewriter_print(
        "If you need to restart the program, just "
        + "type restart."
    )
    typewriter_print(
        "Enter your password length, it needs to be "
        + "a number between 8 and 64. The bigger, the saffer."
    )

    while True:
        try:
            password_length_chosen = input()

            if password_length_chosen == "restart":
                # restart function
                break
            else:
                password_length_chosen = int(password_length_chosen)

            if password_length_chosen > 64 or password_length_chosen < 8:
                raise ValueError

            typewriter_print(
                f"\nGood sutff! Your password length is {password_length_chosen} "
                + "characters long."
            )

            return password_length_chosen

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, it needs to be number between 8 and 64."
            )
            print(Style.RESET_ALL)

welcome_message()
get_length()