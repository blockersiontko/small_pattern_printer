import utils

def draw_diamond(symbol, size):
    for i in range(size):
        print(symbol * (2 * i + 1))
    utils.newLine()

def draw_half_pyramid(symbol, size):
    for i in range(size):
        print(symbol * (i + 1))
    utils.newLine()

patterns = {
    "diamond" : draw_diamond,
    "half-pyramid" : draw_half_pyramid
}