# -*- coding: utf-8 -*-

from getpass        import getpass
from colorama       import init, deinit, Fore
from termcolor      import colored, cprint

from turtle         import Turtle, Driver, Download_Choice

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
    parser.add_argument("-P", "--path", metavar="", help="The path for saving photos.")
    parser.add_argument("-l", "--list", metavar="", help="List of Usernames")
    parser.add_argument("-D", "--download", metavar="", type=int, choices=[1,2], help="Download choice. [1]Update(Default for list) [2]Full")
    parser.add_argument("-v", "--video", metavar="", choices=["True", "False"], default="False", help="Download videos or not. [True]Download [False] Do Not Download(Default)")
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

def header():
    print()
    print_magenta("----------------------------------", "\n\n")
    print_magenta("### Instagram Photo Downloader ###", "\n\n")
    print_magenta("----------------------------------")
    print()

def line():
    print_magenta("-----------------")

def read_json():
    if not os.path.isfile("config.json"):
        return None
    else:
        try:
            with open("config.json") as data_file:
                data = json.load(data_file)
            return data
        except:
            return None

def get_username():
    if args.username:
        return args.username
    else:
        config = read_json()
        if config and config["username"] != "":
            return config["username"]
        else:
            return input("Username : ")

def get_password():
    if args.password:
        return args.password
    else:
        config = read_json()
        if config and config["password"] != "":
            return config["password"]
        else:
            return getpass("Password : ")

def get_path():
    if args.path:
        return args.path
    else:
        config = read_json()
        if config and config["path"] != "":
            return config["path"]
        else:
            return "pictures"

def choose_driver():
    if args.driver == 1:
        driver = Driver.PHANTOM
        print_cyan("Driver : PhantomJS")
    elif args.driver == 2:
        driver = Driver.CHROME
        print_cyan("Driver : Chrome")
    elif args.driver == 3:
        driver = Driver.FIREFOX
        print_cyan("Driver : Firefox")
    else:
        config = read_json()
        if config and "driver" in config and config["driver"] in [1,2,3]:
            _dri = config["driver"]
            if _dri == 1:
                print_cyan("Driver : PhantomJS")
                return Driver.PHANTOM
            elif _dri == 2:
                print_cyan("Driver : Chrome")
                return Driver.CHROME
            elif _dri == 3:
                print_cyan("Driver : Firefox")
                return Driver.FIREFOX

        while True:
            print_cyan("CHOOSE DRIVER : [1]PhantomJS [2]Chrome [3]Firefox")
            d_choice = input("Driver : ")

            if d_choice == "1":
                driver = Driver.PHANTOM
                break
            elif d_choice == "2":
                driver = Driver.CHROME
                break
            elif d_choice == "3":
                driver = Driver.FIREFOX
                break
    return driver

def get_download_choice():
    if args.list:
        if args.download and args.download == 2:
            return Download_Choice.DOWNLOAD_ALL, 0
        else:
            return Download_Choice.UPDATE, 0
    elif args.download:
        if args.download == 2:
            return Download_Choice.DOWNLOAD_ALL, 0
        elif args.download == 1:
            return Download_Choice.UPDATE, 0
    else:
        while True:
            print("How many stories do you want to download?")

            print_magenta("Give number ", "")
            print_cyan("-> For downloading the number of stories")

            print_magenta("Give '0'    ", "")
            print_cyan("-> For downloading all stroies")

            print_magenta("Live empty  ", "")
            print_cyan("-> For downloading last stories you do not have")

            choice = input("Give input : ")

            if choice == "":
                return Download_Choice.UPDATE, 0
            else:
                if RepresentsInt(choice):
                    int_choice = int(choice)
                    if int_choice == 0:
                        return Download_Choice.DOWNLOAD_ALL, 0
                    elif int_choice > 0:
                        return Download_Choice.SOME, int_choice
                    else:
                        print_red("It must be bigger than zero!")
                else:
                    print_red("It must be number or empty!")

def get_video_choice():
    if args.video and args.video == "False":
        return False
    else:
        return True

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def core():
    # Config
    parse_args()
    create_config_if_not_exist()
    init()
    clear_screen()

    # Header
    header()

    # Get info
    driver = choose_driver()
    username = get_username()
    password = get_password()
    path = get_path()
    vid_choice = get_video_choice()

    line()

    # Start Normal Download
    if not args.list:
        t = Turtle()
        t.set_path(path)
        t.open(driver)
        sign_result = t.sign_in(username, password)

        line()

        if sign_result:
            # Get user links
            pic_user = input("Username for Photos : ")
            folder_name = input("Folder name (Leave empty for Instagram username) : ")
            link_result = t.get_img_links(pic_user)

            line()
            if link_result:
                # Download pictures
                down_choice, count = get_download_choice()
                t.download_photos(folder_name, down_choice, count, vid_choice)

        t.close()

    # List Download
    else:
        # Get Json list
        json_path = ""
        if os.path.exists(args.list):
            json_path = args.list
        else:
            print_red("Json path does not exist!")
            return False

        # Open Json list
        with open(json_path, encoding="utf-8") as file:
            data = json.load(file)

            # Instance Turtle and start driver
            t = Turtle()
            t.set_path(path)
            t.open(driver)
            sign_result = t.sign_in(username, password)
            line()

            if sign_result:
                report = {}

                # pic_user loop start
                for pic_user_item in data:
                    # Get user links
                    link_result = t.get_img_links(pic_user_item[1])
                    line()

                    if link_result:
                        # Download pictures
                        down_choice, count = get_download_choice()
                        t.download_photos(pic_user_item[0], down_choice, count, vid_choice)
                        line()

                    # Add download result to Log file
                    if t.result:
                        t.log.append("### RESULT ### TRUE  ### " + pic_user_item[0])
                        report.update({pic_user_item[0] : True})
                    else:                
                        t.log.append("### RESULT ### FALSE ### " + pic_user_item[0])
                        report.update({pic_user_item[0] : False})
                    t.log.append("-------------------------------", False)

                # Add all user report to Log file
                t.log.append("$$ ALL DOWNLOAD RESULT $$")
                t.log.append("-------------------------")
                for key, value in report.items():
                    t.log.append("$$ " + str(value) + " $$ " + str(key) + " $$")
                t.log.append("-------------------------")

            t.close()

if __name__ == "__main__":
    core()