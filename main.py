import os
import secondary as secondary_script
from colorama import Fore


# DEFINE VARIABLES

start_choice = "0"
# First input after starting to select ur mission.

def start_menu():
    global start_choice
    start_choice = "0"
    print("")
    print("----------------------------------------------------------------")
    print(Fore.LIGH.TGREEN_EX + "Welcome to your password manager! v0.69" + Fore.WHITE)
    print("----------------------------------------------------------------")
    print("")
    print(Fore.LIGHTGREEN_EX + "Options:" + Fore.WHITE)
    print("1. List of all your passwords")
    print("2. Create a new password")
    print("3. Delete an old password")
    print("")
    start_choice(input(Fore.LIGHTGREEN_EX + "Press the button according to your choice: " + Fore.WHITE))
    print("")
    print("----------------------------------------------------------------")
    print("")
    return


while start_choice == "1":
    list()
    start_choice = "0"



def start_choice_retry():
    print("")
    print("----------------------------------------------------------------")
    print("")
    print("Invalid Input. Please retry.")
    print("")
    print("----------------------------------------------------------------")
    print("")
    print(Fore.LIGHTGREEN_EX + "Options:" + Fore.WHITE)
    print("1. List of all your passwords")
    print("2. Create a new password")
    print("3. Delete an old password")
    print("")
    start_choice(input(Fore.LIGHTGREEN_EX + "Press the button according to your choice: " + Fore.WHITE))
    print("")
    print("----------------------------------------------------------------")
    print("")

def list():
    print("This is a list")


start_menu()
# secondary_script.export()