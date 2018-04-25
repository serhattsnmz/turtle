# -*- coding: utf-8 -*-

from datetime import datetime
import os
import sys

class Log:

    log_dir  = "logs/"
    log_path = ""

    def __init__(self, log_file_name = datetime.now().strftime("%y-%m-%d_%H-%M-%S")):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.log_path = self.log_dir + log_file_name

        if not os.path.exists(self.log_path):
            f = open(self.log_path, "w")
            f.close()

    def append(self, log_text, write_to_console = True):
        with open(self.log_path, "a", encoding="utf-8") as f:
            date = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            f.write(date + " - " + log_text + "\n")
        if write_to_console:
            print(log_text)

    def append_exception(self, exp, write_to_console = True):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        with open(self.log_path, "a", encoding="utf-8") as f:
            date = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            f.write(date + " - ## (ERROR) : " + str(exp) + " - Type : " + str(exc_type) + " - Line : " + str(exc_tb.tb_lineno) + "\n")
        if write_to_console:
            print("## (ERROR) : " + str(exp) + " - Type : " + str(exc_type) + " - Line : " + str(exc_tb.tb_lineno))