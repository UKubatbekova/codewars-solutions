# https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python

def remove_exclamation_marks(s):
    result = ""
    for i in s:
        if i != "!":
            result += i
    return result