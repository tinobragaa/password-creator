"""
These are the modules used in this project:

time: is a Python module that provides various
time-related functions.

os: is a Python module that provides a way to
interact with the operating system.

sys: is a Python module that provides access to
some variables used or maintained by the interpreter.

random: is a Python module that provides functions
for generating random numbers and sequences.

string: is a Python module that provides various
string-related functions and constants.

pyfiglet: is a third-party Python package that provides
a way to generate ASCII art from text.

colorama: is a third-party Python package that provides
cross-platform support for colored terminal output.

gspread: is a third-party Python package that provides
a way to interact with Google Sheets.

google.oauth2.service_account: is a Python module provided
by the google-auth package that provides support for
authentication using a service account.
"""
import time
import os
import sys
import random
import string
import pyfiglet
from colorama import Fore, Style
import gspread
from google.oauth2.service_account import Credentials

# Code to wire up Google APIs, credit:
# Love Sandwiches Walkthrough Project.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("password_manager")
storage = SHEET.worksheet("storage")


# Code to create the typewriter effect, credit:
# https://stackoverflow.com/questions/20302331/typing-effect-in-python
def typewriter_print(text, speed=0.03):
    """
    This function adds a typewriter effect to the text printed
    to the console. This function iterates over each character
    in the text, writes it to the console, flushes the buffer,
    and waits 0.03s before continuing to the next character.

    Args:
    - text (str): The text to be printed.
    - speed (float): The delay between each character printed.
    Default is 0.03.
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
    This function showcases the welcome message and asks for
    the user's name. It uses a while loop to validate the
    user's input, and raises exceptions if the input is
    invalid. The function returns the user's name.
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
    time.sleep(2)
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
        + "follow three steps:"
    )
    typewriter_print("1 - Choose between 8 and 64 characters long.")
    typewriter_print(
        "2 - Choose a password style: letters only, numbers only or mixed "
        + "characters \n(letters/numbers/symbols)."
    )
    typewriter_print(
        "3 - Choose whether you would like to save your password or not."
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
    This function asks the user to input the desired password
    length and validates the input using a while loop and
    exception handling. The function returns the password
    length as an integer.

    Returns:
    - int: The length of the password chosen by the user.
    """
    typewriter_print(
        "Enter your password length, it needs to be "
        + "a number between 8 and 64. \nThe bigger, the safer.\n"
    )

    while True:
        try:
            password_length_chosen = input()

            if password_length_chosen == "exit":
                exit_generator()
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


def get_style(password_length_chosen):
    """
    This function asks the user to choose the desired password style
    (letters only, numbers only, or mixed characters), and validates
    the input using a while loop and exception handling. The
    function returns the chosen style as an integer.

    Args:
    - password_length_chosen: An integer representing the length of
    the password.

    Returns:
    - An integer representing the chosen style: 1 for letters only,
    2 for numbers only, and 3 for mixed characters.
    """

    typewriter_print(
        "Which characters would you like to have in your password? "
        + "\nRemember: the more complex the safer!"
    )
    typewriter_print("1 - Letters only.")
    typewriter_print("2 - Numbers only.")
    typewriter_print("3 - Mixed characters: letters, numbers and symbols.\n")

    while True:
        try:
            password_style = input()
            if password_style == "exit":
                exit_generator()
            else:
                password_style = int(password_style)

            if not 1 <= password_style <= 3:
                raise ValueError

            if password_style == 1:
                typewriter_print(
                    f"\nHmm, you chose {password_style} so your password "
                    + "style will contain letters only and will be \n"
                    + f"{password_length_chosen} characters long."
                )
            elif password_style == 2:
                typewriter_print(
                    f"\nOkey-dokey, you chose {password_style} so your "
                    + "password will contain numbers only and will be \n"
                    + f"{password_length_chosen} characters long."
                )
            else:
                typewriter_print(
                    f"\nSounds safe, you chose {password_style} so your "
                    + "password will contain letters, numbers and\nsymbols "
                    + f"and will be {password_length_chosen} characters long."
                )
            time.sleep(3)

            return password_style

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, please choose 1, 2 or 3."
            )
            print(Style.RESET_ALL)


def create_password(password_style, password_length_chosen):
    """
    This function generate a random password of the specified style and length.

    Args:
    - password_style (int): The style of the password to generate.
    - password_length_chosen (int): The length of the password to generate.

    Returns:
    - str: A random password of the specified style and length.
    """
    if password_style == 1:
        # Generate a password with letters only.
        password = ''.join(
            random.choices(string.ascii_letters, k=password_length_chosen)
        )
    elif password_style == 2:
        # Generate a password with numbers only.
        password = ''.join(
            random.choices(string.digits, k=password_length_chosen))
    elif password_style == 3:
        # Generate a password with letters, numbers, and symbols.
        password = ''.join(
            random.choices(
                string.ascii_letters
                + string.digits
                + string.punctuation,
                k=password_length_chosen
            )
        )

    return password


def display_password(password):
    """
    This function takes a 'password' parameter and displays it to the user
    in a formatted and visually appealing way. It also prompts the user to
    start again or exit the password generator.

    Args:
    - password (str): The generated password to be displayed.
    """
    clear_terminal()
    typewriter_print("\nYour password is being created...")
    typewriter_print(
        "\nCounting the number of atoms in the universe... okay, not really, "
        + "just making \nsure your password is strong enough..."
    )
    time.sleep(.8)
    typewriter_print(
        "\nChecking for loopholes... and finding none, sorry hackers..."
    )
    time.sleep(.8)
    typewriter_print(
        "\nGenerating random characters... don't worry, they're "
        + "very friendly..."
    )
    time.sleep(.8)
    typewriter_print("\nYour password is now ready:\n")
    time.sleep(.8)
    typewriter_print(
        Fore.LIGHTBLUE_EX
        + password
    )
    print(Style.RESET_ALL)
    time.sleep(1)
    typewriter_print("Would you like to save your password? ( Y / N )")

    while True:
        try:
            save_password = input()
            if save_password == "exit":
                time.sleep(1)
                exit_generator()
            elif save_password in ("y", "Y"):
                time.sleep(2)
                return True
            elif save_password in ("n", "N"):
                time.sleep(1)
                break
            else:
                raise ValueError
            return

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, please choose Y or N."
            )
            print(Style.RESET_ALL)

    typewriter_print("Would you like to start again? ( Y / N )")

    while True:
        try:
            reset = input()
            if reset in ("y", "Y"):
                time.sleep(1)
                clear_terminal()
                os.system("python3 'run.py'")
            elif reset in ("n", "N", "exit"):
                time.sleep(1)
                exit_generator()
            else:
                raise ValueError
            return

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, please choose Y or N."
            )
            print(Style.RESET_ALL)


def store_password(password):
    """
    This function save the created password along with the corresponding
    username and URL to a Google Spreadsheet. The function prompts the
    user to enter their username and URL, and appends a new row to the
    spreadsheet with these details and the provided password.

    Args:
    - password (str): The generated password to be saved.
    """
    clear_terminal()
    print(
        Fore.CYAN
        + "================================"
        + Style.RESET_ALL
    )
    print("\nWelcome to the Password Manager!\n")
    print(
        Fore.CYAN
        + "================================"
        + Style.RESET_ALL
    )
    typewriter_print(
        "A place where you can store your login information with the "
        + "password you just \ncreated!"
    )
    typewriter_print(
        "We just need your username and URL. We'll guard your details "
        + "so you don't need \nto worry!"
    )
    typewriter_print(
        "The password you created is:\n"
        + Fore.BLUE
        + f"{password}"
        + Style.RESET_ALL
        + "."
    )

    typewriter_print("Enter your username:\n")

    while True:
        username = ""
        try:
            username = input()
            if username == "exit":
                time.sleep(1)
                exit_generator()
            elif username == "":
                raise ValueError("username cannot be blank.")
            elif len(username) < 3:
                raise ValueError("a minimum of 3 characters.")
            else:
                break

        except ValueError as error:
            print(
                Fore.LIGHTRED_EX
                + f"\nTry again, {error}"
            )
            print(Style.RESET_ALL)

    typewriter_print("\nEnter the URL:\n")

    while True:
        url = ""
        try:
            url = input()
            if url == "exit":
                time.sleep(1)
                exit_generator()
            elif url == "":
                raise ValueError("username cannot be blank.")
            elif len(url) < 3:
                raise ValueError("a minimum of 3 characters.")
            else:
                break

        except ValueError as error:
            print(
                Fore.LIGHTRED_EX
                + f"\nTry again, {error}"
            )
            print(Style.RESET_ALL)

    new_row = [url, username, password]
    storage.append_row(new_row)
    typewriter_print(
        "\nThe URL, username, and password have been added to our database!"
    )

    typewriter_print("Would you like to start again? ( Y / N )")

    while True:
        try:
            reset = input()

            if reset in ("y", "Y"):
                time.sleep(1)
                clear_terminal()
                os.system("python3 'run.py'")
            elif reset in ("n", "N", "exit"):
                time.sleep(1)
                exit_generator()
            else:
                raise ValueError
            return

        except ValueError:
            print(
                Fore.LIGHTRED_EX
                + "\nTry again, please choose Y or N."
            )
            print(Style.RESET_ALL)


def exit_generator():
    """
    This function prints a warning message and exit the program.
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
    time.sleep(2)
    clear_terminal()
    sys.exit()


def main_function():
    """
    This function is responsible to control the flow of the program
    and print out the password created.
    """
    welcome_message()
    password_length_chosen = get_length()
    password_style = get_style(password_length_chosen)
    password = create_password(password_style, password_length_chosen)
    display_password(password)
    store_password(password)


main_function()
