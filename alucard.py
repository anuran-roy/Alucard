import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

from transylvania import ExecutionEngine
from voice import Speech2Command
from dracula import Wolfram
from aesthetics import colors

engine = ExecutionEngine()
print("\n")
while True:
    try:
        print(f"\n{colors['WHITE']}Alucard > ", end='')
        cmd = input()
        engine.addHistory(cmd)
        engine.addVar(cmd)
    except KeyboardInterrupt:
        engine.saveHistory()
        print(f"{colors['WARNING']}\n\nCtrl + C pressed! Exiting Alucard...\n")
        break
