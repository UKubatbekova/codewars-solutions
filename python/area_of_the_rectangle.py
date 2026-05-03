# https://www.codewars.com/kata/580a0347430590220e000091/train/python

import math
def area(d, l):
    return "Not a rectangle" if d <= l else l * math.sqrt(d ** 2 - l ** 2)