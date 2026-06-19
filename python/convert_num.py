# https://www.codewars.com/kata/57cded7cf5f4ef768800003c/train/python

def convert_num(number, base):
    if isinstance(number, int) and base == 'hex':
        return hex(number)
    elif isinstance(number, int) and base == 'bin':
        return bin(number)
    elif type(number) != int:
        return "Invalid number input"
    elif base != "hex" or base != "bin":
        return "Invalid base input"