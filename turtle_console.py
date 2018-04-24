# -*- coding: utf-8 -*-

from colorama       import init, deinit, Fore
from termcolor      import colored, cprint

import os
import json
import platform
import argparse

print_red       = lambda x, y="\n" : cprint(x, "red", end=y)
print_green     = lambda x, y="\n" : cprint(x, "green", end=y)
print_magenta   = lambda x, y="\n" : cprint(x, "magenta", end=y)
print_yellow    = lambda x, y="\n" : cprint(x, "yellow", end=y)
print_cyan      = lambda x, y="\n" : cprint(x, "cyan", end=y)

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch all the lectures for a Instagram")
    parser.add_argument("-u", "--username", metavar="", help="User username")
    parser.add_argument("-p", "--password", metavar="", help="User password")
    parser.add_argument("-d", "--driver",   metavar="", type=int, choices=[1,2,3], help="Choosen Driver. [1]PantomJS [2]Chrome [3]Firefox")
    parser.add_argument("--path", metavar="", help="The path for saving photos.")
    parser.add_argument("-l", "--list", metavar="", help="List of Usernames")
    global args 
    args = parser.parse_args()

def clear_screen():
    plt = platform.system()
    
    if plt == "Windows":
        os.system("cls")
    elif plt == "Linux":
        os.system("clear")

def create_config_if_not_exist():
    if not os.path.isfile("config.json"):
        try:
            data = {"username" : "", "password" : "", "path" : "pictures"}
            text = json.dumps(data)
            with open("config.json", "w") as file:
                file.write(text)
        except:
            print_red("Config file could not be created!")
            print_yellow("Try run this script as root.")
            return

def core():
    parse_args()
    create_config_if_not_exist()
    init()
    clear_screen()

    header()

if __name__ == "__main__":
    core()