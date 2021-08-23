import json
from pprint import pprint

import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from aesthetics import colors

class SessionData:

    def __init__(self):
        self.history = open("commands.txt", "r").read().split("\n")
        self.var = {}
        self.line = None

    def addHistory(self, line):
        self.line = line.strip()
        self.history.append(line)

        if line.lower() == "history":
            print(f"{colors['OKGREEN']}\n-----------\n")
            print(f"{colors['OKGREEN']}\nCOMMAND HISTORY:\n")
            for i in self.history:
                print(f"{colors['OKGREEN']}{i}")
            print(f"{colors['OKGREEN']}\n-----------\n")

        if line.lower() == "stack":
            print(f"{colors['OKGREEN']}\n-----------\n")
            print(f"{colors['OKGREEN']}\nVARIABLE STACK:\n")
            for i in self.var.keys():
                print(f"{colors['OKGREEN']}{i}: {self.var[i]}")
            print(f"{colors['OKGREEN']}\n-----------\n")

    def saveHistory(self):
        f = open("commands.txt", "w")
        
        for i in self.history:
            f.write(i)
            f.write("\n")
        
        f.close()
    



