# -*- coding: utf-8 -*-

from selenium       import webdriver
from getpass        import getpass
from urllib.request import urlretrieve
from time           import sleep
from datetime       import datetime
from turtle_log     import Log

import os
import json

class Driver:
    PHANTOM = 1
    CHROME  = 2
    FIREFOX = 3

class Turtle:

    _user_username   = ""
    _user_password   = ""
    _pic_path        = ""
    _driver          = None
    log              = None

    imgLinks    = []

    def __init__(self, username, password, pic_path = "pictures"):
        self._user_username = username
        self._user_password = password
        self._pic_path = pic_path

    # Open driver and Log
    def open(self, driver_choice = Driver.PHANTOM):
        try:
            self._set_driver(driver_choice)
            self.log = Log(str(datetime.now()))
            
            self.log.append("NEW OBJECT CREATED!")
            self.log.append("User : " + self._user_username + " - Driver : " + str(driver_choice))
        except Exception as exp:
            self.log.append_exception(exp)

    # Close driver and remove cookies
    def close(self):
        try:
            self._driver.delete_all_cookies()
            self._driver.quit()
            self.log.append("Browser closed successfuly.")
        except Exception as exp:
            self.log.append_exception(exp)

    # return : webdriver
    def _set_driver(self, driver_choice):
        if driver_choice == Driver.CHROME:
            self._driver = webdriver.Chrome()
        elif driver_choice == Driver.FIREFOX:
            self._driver = webdriver.Firefox()
        else:
            self._driver = webdriver.PhantomJS()
        return self._driver

    # return : True or False
    def sign_in(self):
        try:
            self._driver.get("https://www.instagram.com/")
            sleep(2)

            # Pass the sign-up page
            try:
                self._driver.find_element_by_css_selector("._g9ean a").click()
            except:
                pass
            
            # Send user info
            self._driver.find_element_by_name("username").send_keys(self._user_username)
            self._driver.find_element_by_name("password").send_keys(self._user_password)
            self._driver.find_element_by_tag_name("button").click()   
            sleep(4)

            # If there is 2 factor verification
            try:
                self._driver.find_element_by_name("verificationCode")
                self.log.append("Username and Password are correct.")
                self.log.append("## Verification Found!")
                return False
            except:
                pass
            
            try:
                self._driver.find_element_by_class_name("coreSpriteSearchIcon")
                self.log.append("Username and Password are correct.")
                return True
            except:
                pass
        
            self.log.append("## Username or Password are NOT CORRECT!")
            return False
        except Exception as exp:
            self.log.append_exception(exp)
            return False

    # return : imgLinks [] or False
    def get_img_links(self, pic_user):
        try:
            if not pic_user:
                self.log.append("## Username must be given for finding photos!")
                return False
                
            self.log.append("Getting user...")
            self._driver.get("https://www.instagram.com/" + pic_user)
            
            self.log.append("Listing stories...")
            
            photo_total = int(self._driver.find_element_by_class_name("_fd86t").text.replace(".", "").replace(",",""))
            imgLinks = []
            count = 0
            error = 0

            while len(imgLinks) != photo_total:
                # Find all photos of current page
                imgList = self._driver.find_elements_by_css_selector("._mck9w a")
                
                # Add the photos to list if not exists
                for idx, img in enumerate(imgList):
                    _link = img.get_property("href")
                    if not _link in imgLinks:
                        imgLinks.append(_link)
                
                # Write current link count to log
                if len(imgLinks) % 10 != count:
                    count = len(imgLinks) % 10
                    self.log.append(str(len(imgLinks)) + " photos found.")
                else:
                    # This means collection is not working!
                    error += 1

                # If program stops  to collect links> then break while
                if error == 10:
                    self.log.append("## Circle broken for user : " + pic_user)
                    break
                
                # Scroll down the picture
                self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)

            self.log.append("> " + str(len(imgLinks)) + " < links found.")
            return imgLinks
        except Exception as exp:
            self.log.append_exception(exp)
            return False