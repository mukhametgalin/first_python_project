import os
import random

def clean_console():
    os.system('clear')


def generate_text():
    chars = []
    for i in range(ord('a'), ord('z') + 1):
        chars.append(chr(i))
    for i in range(ord('A'), ord('A') + 1):
        chars.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        chars.append(chr(i))
    chars.append(' ')

    default_size = 20

    result = ""

    for i in range(default_size):
        result = result + chars[random.randrange(0, len(chars))]

    while result[-1] == ' ':
        result.pop()

    while result[0] == ' ':
        result.pop(0)

    return result