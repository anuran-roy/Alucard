# This is the command parser for Alucard.AI

import sys  
# from pathlib import Path  
# file = Path(__file__). resolve()  
# package_root_directory = file.parents [1]  
# sys.path.append(str(package_root_directory))

import yaml
from sessiondata import SessionData
from dracula import Wolfram
from aesthetics import colors
from subprocess import call
# from dracula import Wolfram
import os

class ExecutionEngine(Wolfram, SessionData):
    """
    This is the aggregation class of all the features in Alucard.ai.
    Any executable feature must be a base class for this class.
    """

    def __init__(self):
        super(ExecutionEngine, self).__init__()

        self.environment_commands = {
            "clear": "call('clear' if os.name =='posix' else 'cls')",
            "exit": "sys.exit(0)",

        }
        self.engineconfig = yaml.safe_load(open("config.yaml", "r"))

    def execute(self, to_exec, mode='print'):
        self.line = to_exec.strip()

        if self.line in self.environment_commands.keys():
            return exec(self.environment_commands[self.line])

        elif self.line[:self.line.find(" ")] in self.engineconfig.values(): # Add all the engines to it
            self.chosenEngine = self.line[:self.line.find(" ")]
            self.command = self.line[self.line.find(" ")+1:].strip()
            self.output = None

            ################### WOLFRAM ENGINE ###################

            if self.chosenEngine == self.engineconfig['WOLFRAM']: 
                self.output = self.wolfram_run(self.command)                
                if mode == 'print':
                    print(self.output)
                elif mode == 'value':
                    return self.output
            
            ################### WOLFRAM ALPHA ENGINE ###################

            if self.chosenEngine == self.engineconfig['WOLFRAM-ALPHA']: # Code for the Wolfram Alpha Engine
                self.output = self.walpha_run(self.command)
                # print(self.line[:self.line.find(" ")])
                if mode == 'print':
                    print(self.output)
                elif mode == 'value':
                    return self.output
            
        else:
            if mode == 'print':
                print(f"{exec(self.line)}")
            else:
                return exec(self.line)

    def addVar(self, line):
        self.line = line.strip()
        ls = None
        # try:
        if "<-" in self.line:
            ls = [x.strip() for x in line.split("<-")]
            print(f"Assigning {ls[1]} to object {ls[0]}...")
            if self.execute(ls[1]) is None:
                self.var[ls[0]] = ls[1]
        else:
            print(f"Executing without assignment...")
            # if self.line not in self.environment_commands.keys() and (self.line[:self.line.find(" ")] not in list(self.engineconfig.values())): 
            #     self.execute(f"print('{self.line}')")
            # else:
            self.execute(self.line)
    
        if ls is not None:
            print(f"\n\n{colors['OKGREEN']}{ls[0]} = {self.var[ls[0]]}\n")
            
        # except Exception as e:
        # print(f"{colors['FAIL']}Error logging variable into the variable stack. Details: {e}")

        

