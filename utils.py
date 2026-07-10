import os
from colorama import Fore, Style

def newLine():
    print()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def resetStyle():
    print(Style.RESET_ALL)

def redText():
    redText = Fore.RED
    return redText