# https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python

def correct_polish_letters(st):
    result = ""
    for i in st:
        if i == 'ą':
            result += "a"
        elif i == 'ć':
            result += "c"
        elif i == 'ę':
            result += "e"
        elif i == 'ł':
            result += "l"
        elif i == 'ń':
            result += "n"
        elif i == 'ó':
            result += "o"
        elif i == 'ś':
            result += "s"
        elif i == 'ź':
            result += "z"
        elif i == 'ż':
            result += "z"
        else:
            result += i
    return result