import utils

def draw_diamond(symbol, size):

    size = lowInput(size)

    width = 2 * size - 1

    for i in range(size):
        print(f"{symbol * (2 * i + 1):^{width}}")

    for i in range(size - 2, -1, -1):
        print(f"{symbol * (2 * i + 1):^{width}}")
    utils.newLine()

def draw_pyramid(symbol, size):

    size = lowInput(size)

    width = 2 * size - 1

    for i in range(size):
        print(f"{symbol * (2 * i + 1):^{width}}")
    utils.newLine()

def draw_huge_pyramid(symbol, size):

    if size > 20:
        size = 20
        print(utils.redText() + "UWAGA! Dla wzoru huge pyramid maksymalny rozmiar to 20! Aktualizuję rozmiar na 20.")
        utils.resetStyle()
    
    size = lowInput(size)

    width = 8 * size - 1

    for i in range(size):
        print(f"{symbol * (8 * i + 1):^{width}}")
    utils.newLine()

def lowInput(size):
    if size == 0:
        size = 1
        print(utils.redText() + "UWAGA! Dla wszystkich wzorów minimalny rozmiar to 1. Aktualizuję rozmiar na 1.")
        utils.resetStyle()
    return size

patterns = {
    "diamond" : draw_diamond,
    "pyramid" : draw_pyramid,
    "huge pyramid" : draw_huge_pyramid
}
