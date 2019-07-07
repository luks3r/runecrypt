#
# God language crypt machine
#

# Imports
import os
import random
import string
from libs.utils import *

default_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
default_pattern = "ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹᚺᚻᚼᚽᚾᚿᛀᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛠᛡᛢᛣᛤᛥᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯᛰ"

# Generate dictionary that is used for cryprting
def genDict(seed, backwards = False, alphabet = default_alphabet, pattern = default_pattern):
    if len(alphabet) > len(pattern):
        print("Alphabet - {0}, Pattern - {1}".format(len(alphabet), len(pattern)))
        print("Alphabet can't be shorter than pattern!")
        return
    random.seed(seed)
    dictionary = {}

    shuffledAlphabet = stringShuffle(alphabet, seed)
    shuffledPattern = stringShuffle(pattern, seed)

    for i in range(0, len(shuffledAlphabet)):
        dictionary[shuffledAlphabet[i]] = shuffledPattern[i]

    if backwards:
        dictionary = backward_dictionary(dictionary)

    return dictionary

# Mirror the dictionary
def backward_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

# Encrypt the string
def encrypt(string, seed, alphabet = default_alphabet, pattern = default_pattern):
    dictionary = genDict(seed, False, alphabet, pattern)
    result = ""

    for s in string:
        if s in dictionary: result += dictionary[s]
        else: result += s

    return result

def crypt(string, seed, alphabet = default_alphabet, pattern = default_pattern):
    return encrypt(string, seed, alphabet, pattern)

# Decrypt the string
def decrypt(string, seed, alphabet = default_alphabet, pattern = default_pattern):
    dictionary = genDict(seed, True, alphabet, pattern)
    result = ""

    for s in string:
        if s in dictionary: result += dictionary[s]
        else: result += s

    return result

# User CLI for cryptor
def cli():
    running = True

    while running:
        entered = input("Действия: 1 - Зашифровать, 2 - Расшифровать >> ")

        if entered == "1":
            seed = input("Введите ключ шифрования >> ")
            print("Введите текст для зашифровки")
            text = input(">> ")

            try:
                print(encrypt(text, seed))
            except:
                print("Ошибка!")
        elif entered == "2":
            seed = input("Введите ключ шифрования >> ")
            print("Введите текст для расшифровки")
            text = input(">> ")

            try:
                print(decrypt(text, seed))
            except:
                print("Ошибка!")
        else:
            running = False

# Main function
def main():
    try:
        cli()
    except:
        exit(0)

# Test function
def test():
    a = "abcedr"

# If it is started as main file (not library), it starts the main function
if __name__ == "__main__":
    env = os.environ.get('PY_ENV')
    if env == None or env == "production":
        main()
    elif env == "test" or env == "staging" or env == "development":
        test()
    else:
        print("No such environment!")
        exit(1)