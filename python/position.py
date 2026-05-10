# https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python

import string

def position(letter):
    alphabet = string.ascii_lowercase
    position = alphabet.index(letter.lower()) + 1
    return "Position of alphabet: " + str(position)