# Import necessary modules.
import time
import os
import sys
import random
import string
import pyfiglet
from colorama import Fore, Style


# Code to create the typewriter effect, credit:
# https://stackoverflow.com/questions/20302331/typing-effect-in-python
def typewriter_print(text, speed=0.03):
    """
    This function add the typewriter effect.
    """
    print(Style.RESET_ALL)
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
    and lead to the get_length function.
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
        "If you need to close the program, just "
        + "type exit."
    )
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
        "2 - Choose letter only or mixed characters (letters/numbers/symbols)."
    )
    typewriter_print("First things first, enter your name:\n")

    while True:
        user_name = ""
        try:
            user_name = input()

            if user_name == "exit":
                exit_generator()

            elif user_name == "":
                raise ValueError("name cannot be blank.")

            elif user_name.isdigit():
                raise ValueError("letters only.")

            elif len(user_name) < 3:
                raise ValueError("a minimum of 3 characters.")

            elif len(user_name) > 16:
                raise ValueError("a maximum of 16 characters.")

            else:
                typewriter_print(
                    f"\nHi {user_name}, let's make your unique password!"
                )
                time.sleep(2.5)
                clear_terminal()

            return user_name

        except ValueError as error:
            print(Fore.LIGHTRED_EX + f"\nTry again, {error}")
            print(Style.RESET_ALL)


def get_length():
    """
    This function takes the password length chosen
    by the user. The user's input will be stored as
    an integer and needs to be a number between
    8 and 64, otherwise will raise an exception.
    """
    typewriter_print(
        "Enter your password length, it needs to be "
        + "a number between 8 and 64. The bigger, the saffer.\n"
    )

    while True:
        try:
            password_length_chosen = input()

            if password_length_chosen == "exit":
                exit_generator()
                break
            else:
                password_length_chosen = int(password_length_chosen)

            if password_length_chosen > 64 or password_length_chosen < 8:
                raise ValueError

            typewriter_print(
                f"\nNice! Your password length is {password_length_chosen} "
                + "characters long."
            )

            return password_length_chosen

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, choose a number between 8 and 64."
            )
            print(Style.RESET_ALL)


def get_style():
    """
    This function takes the password style chosen
    by the user. The user's input will be stored as
    an integer and needs to be 1 or 2, otherwise
    will raise an exception.
    """

    typewriter_print(
        "What characters would you like to have your password? "
        + "Remember: the more complex the safer!"
    )
    typewriter_print("1 - Letters only.")
    typewriter_print("2 - Mixed characters: letters, numbers and symbols.\n")

    while True:
        try:
            password_style = input()

            if password_style == "exit":
                exit_generator()
                break
            else:
                password_style = int(password_style)

            if not 1 <= password_style <= 2:
                raise ValueError

            if password_style == 1:
                typewriter_print(
                    f"\nHmm, you chose {password_style} so your password "
                    + "style will contain letters only."
                )
            else:
                typewriter_print(
                    f"\nSounds safe, you chose {password_style} so your "
                    + "password will contain letters, numbers and symbols."
                )

            return password_style

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, please choose 1 or 2."
            )
            print(Style.RESET_ALL)


def create_password(password_style, password_length_chosen):
    """
    This function creates a random and unique password. It takes
    two parameters: password length and password style from the
    previous functions.
    """
    if password_style == 1:
        # Generate a password with letters only
        password = ''.join(
            random.choices(string.ascii_letters, k=password_length_chosen)
        )

    if password_style == 2:
        # Generate a password with letters, numbers, and symbols
        password = ''.join(
            random.choices(
                string.ascii_letters
                + string.digits
                + string.punctuation,
                k=password_length_chosen
            )
        )

    return password


def exit_generator():
    """
    This function prints a warning message and
    exit the program.
    """
    clear_terminal()
    typewriter_print("The program will exit in...")
    typewriter_print("3... \n")
    time.sleep(1)
    typewriter_print("2... \n")
    time.sleep(1)
    typewriter_print("1... \n")
    time.sleep(.5)
    typewriter_print("The program is now closed.")
    time.sleep(3)
    clear_terminal()
    sys.exit()


def main_function():
    """
    This function is responsible to control the flow of the program
    and print out the password created.
    """
    welcome_message()
    password_length_chosen = get_length()
    password_style = get_style()
    password = create_password(password_style, password_length_chosen)
    print(password)


main_function()
