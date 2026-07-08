import symbols
import patterns
import os

class PatternPrinter:
    def __init__(self):
        self.findSymbolLoop = True
        self.findPatternLoop = True
        self.findSymbol()
        self.findPattern()

    def findSymbol(self):

        while self.findSymbolLoop:
            self.newLine()
            self.printSymbolList()
            self.newLine()
            symbol_input = input("Wybierz symbol z listy: ")

            if not symbol_input.isdigit() or int(symbol_input) >= len(symbols.symbols):
                self.clearTerminal()
                self.err_InputNotFound()
                continue

            if symbol_input and int(symbol_input) < len(symbols.symbols):
                index = int(symbol_input)
                nazwa, znak = list(symbols.symbols.items())[index]

                self.newLine()
                print(nazwa)
                print(znak)
                self.clearTerminal()

                symbolConfirm = input(f"{znak} - czy chcesz wybrać ten symbol? Y/N\n").strip().upper()
                if symbolConfirm == "N":
                    continue
                elif symbolConfirm == "Y":
                    self.findSymbolLoop = False
                    break
                else:
                    self.clearTerminal()
                    self.err_InputNotFound()
                    continue

            else:
                self.clearTerminal()
                self.err_InputNotFound()
                continue

    def findPattern(self):

        while self.findPatternLoop:
            self.newLine()
            self.printPatternList()
            self.newLine()
            pattern_input = input("Wybierz pattern z listy: ")

            if not pattern_input.isdigit() or int(pattern_input) >= len(patterns.patterns):
                self.clearTerminal()
                self.err_InputNotFound()
                continue

            if pattern_input and int(pattern_input) < len(patterns.patterns):
                jndex = int(pattern_input)
                pattern = list(patterns.patterns)[jndex]

                self.newLine()
                print(pattern)
                self.clearTerminal()

                patternConfirm = input(f"{pattern} - czy chcesz wybrać ten pattern? Y/N\n").strip().upper()
                if patternConfirm == "N":
                    continue
                elif patternConfirm == "Y":
                    self.findPatternLoop = False
                    break
                else:
                    self.clearTerminal()
                    self.err_InputNotFound()
                    continue


    def printSymbolList(self):
        for i, (_name, _symb) in enumerate(symbols.symbols.items()):
            symbolsInTerminal = f"{i}. '{_name}' - '{_symb}'"
            print(symbolsInTerminal)

    def printPatternList(self):
        for j, _patt, in enumerate(patterns.patterns):
            patternsInTerminal = f"{j}. '{_patt}'"
            print(patternsInTerminal)

    def newLine(self):
        print()

    def clearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def err_InputNotFound(self):
        print("Nieprawidłowy input! Wracam do poprzedniego ekranu.")

if __name__ == "__main__":
    PatternPrinter()