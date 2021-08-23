# This is the command parser for Alucard.AI

import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import yaml
from sessiondata import SessionData
from dracula import Wolfram
from aesthetics import colors
import os


class ExecutionEngine(SessionData, Wolfram):
    
    def __init__(self):
        super(ExecutionEngine, self).__init__()

        self.environment_commands = {
            "clear": "",
            "exit": "",

        }
        # self.wolfram_commands = []
        self.config = yaml.safe_load(open("config.yaml", "r"))
        # self.line = None

    def execute(self, to_exec):
        # try:
        if self.line in self.environment_commands.keys():
            return exec(self.environment_commands[self.line])
        elif self.line[:self.line.index(" ")] == self.config['WOLFRAM']:
            return self.session.evaluate(self.line[self.line.index(" "):].strip())
        else:
            return eval(self.line)
        # except Exception as e:
        print(f"{colors['FAIL']}An exception occured. Details: \n{e}", end="")
        print(f"{colors['WHITE']}")

    def addVar(self, line):
        self.line = line.strip()
        ls = None
        try:
            if "<-" in self.line:
                ls = line.split("<-")
                print(f"Assigning to {ls[1].strip()} an object {ls[0].strip()}...")
                self.var[ls[0].strip()] = self.execute(ls[1].strip())
            else:
                print(f"Executing without assignment...")
                self.execute(line.strip())
        
            if ls is not None:
                print(f"\n\n{colors['OKGREEN']}{ls[0].strip()} = {self.var[ls[0].strip()]}\n")
            
        except Exception as e:
            print(f"{colors['FAIL']}Error logging variable into the variable stack. Details: {e}")

        

