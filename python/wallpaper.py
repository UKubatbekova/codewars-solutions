# https://www.codewars.com/kata/567501aec64b81e252000003/train/python

import math

def wallpaper(l, w, h):
    if l == 0 or w == 0 or h == 0:
        return numbers[0]
    else:
        wall_area = 2 * h * (l+w)
        needed = wall_area * 1.15
        result = math.ceil(needed / 5.2)
        return numbers[result]