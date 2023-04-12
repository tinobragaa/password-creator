#Password Creator: Password generator created for my PP3.

import random

import time

from colorama import Fore, Style

def welcome_message():
    """
    This function showcase the welcome message,
    logo design, explain what the program is
    and lead to the get_user_name function.
    """
    print(Fore.WHITE + "==============================================")
    time.sleep(.5)
    print(Fore.WHITE + "\nWecome to the password creator!\n")
    print(Fore.WHITE + "Create a unique password with a hard-to-hack tech.\n")
    print(Fore.WHITE + "==============================================")

welcome_message()