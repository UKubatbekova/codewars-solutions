# https://www.codewars.com/kata/596fba44963025c878000039/train/python

def contamination(text, char):
    new_string = ''
    for i in range(len(text)):
        new_string += char
    return new_string