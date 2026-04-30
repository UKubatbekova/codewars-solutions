# https://www.codewars.com/kata/574758e396b130b63e00069b

def polygon_area(a, b, c, d):
    triangle = 1/2 * b * (c - a)
    rectangle = a * b
    return triangle + rectangle