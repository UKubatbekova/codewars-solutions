# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python

def close_compare(a, b, margin=0):
    abs_distance = a - b
    if margin >= abs(abs_distance):
        return 0
    elif a < b:
        return -1
    else:
        return 1