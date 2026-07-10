import symbols
import patterns
import utils

class PatternPrinter:
    def __init__(self):
        self.findSymbolLoop = True
        self.findPatternLoop = True
        self.findSymbol()
        self.findPattern()
        self.executePattern()

    def findSymbol(self):

        while self.findSymbolLoop:
            utils.newLine()
            self.printSymbolList()
            utils.newLine()
            symbol_input = input("Wybierz symbol z listy: ")

            if not symbol_input.isdigit() or int(symbol_input) >= len(symbols.symbols):
                utils.clearTerminal()
                self.err_InputNotFound()
                continue

            if symbol_input and int(symbol_input) < len(symbols.symbols):
                index = int(symbol_input)
                nazwa, znak = list(symbols.symbols.items())[index]

                utils.newLine()
                print(nazwa)
                print(znak)
                utils.clearTerminal()

                symbolConfirm = input(f"{znak} - czy chcesz wybrać ten symbol? Y/N\n").strip().upper()
                if symbolConfirm == "N":
                    continue
                elif symbolConfirm == "Y":
                    self.selectedSymbol = znak
                    self.findSymbolLoop = False
                    break
                else:
                    utils.clearTerminal()
                    self.err_InputNotFound()
                    continue

            else:
                utils.clearTerminal()
                self.err_InputNotFound()
                continue

    def findPattern(self):

        while self.findPatternLoop:
            utils.newLine()
            self.printPatternList()
            utils.newLine()
            pattern_input = input("Wybierz pattern z listy: ")

            if not pattern_input.isdigit() or int(pattern_input) >= len(patterns.patterns):
                utils.clearTerminal()
                self.err_InputNotFound()
                continue

            if pattern_input and int(pattern_input) < len(patterns.patterns):
                jndex = int(pattern_input)
                pattern_name, pattern_function = list(patterns.patterns.items())[jndex]

                utils.newLine()
                print(pattern_name)
                utils.clearTerminal()

                patternConfirm = input(f"{pattern_name} - czy chcesz wybrać ten pattern? Y/N\n").strip().upper()
                if patternConfirm == "N":
                    continue
                elif patternConfirm == "Y":
                    self.selectedPatternFunction = pattern_function
                    self.findPatternLoop = False
                    break
                else:
                    utils.clearTerminal()
                    self.err_InputNotFound()
                    continue

    def executePattern(self):
        utils.clearTerminal()
        sizeInput = input("Podaj rozmiar wzoru: ")
        utils.newLine()

        if not sizeInput.isdigit():
            utils.clearTerminal
            self.err_InputNotFound()
            input("Naciśnij Enter, by spróbować ponownie...")
            return self.executePattern()
        
        size = int(sizeInput)
        utils.newLine()
        self.selectedPatternFunction(self.selectedSymbol, size)

    def printSymbolList(self):
        for i, (_name, _symb) in enumerate(symbols.symbols.items()):
            symbolsInTerminal = f"{i}. '{_name}' - '{_symb}'"
            print(symbolsInTerminal)

    def printPatternList(self):
        for j, _patt in enumerate(patterns.patterns):
            patternsInTerminal = f"{j}. '{_patt}'"
            print(patternsInTerminal)

    def err_InputNotFound(self):
        print("Nieprawidłowy input! Wracam do poprzedniego ekranu.")

if __name__ == "__main__":
    PatternPrinter()