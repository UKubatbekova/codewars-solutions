# https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python

def remainder(a,b):
    max_value = 0
    min_value = 0
    if a > b:
        max_value += a
        min_value += b
    else:
        max_value += b
        min_value += a
    return None if min_value == 0 else max_value % min_value