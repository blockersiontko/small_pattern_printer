import os

def newLine():
    print()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')