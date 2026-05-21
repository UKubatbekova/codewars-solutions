# https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python

import math

def calculate_tip(amount, rating):
    if rating.casefold() == 'terrible':
        return amount * 0 / 100
    elif rating.casefold() == 'poor':
            return math.ceil(amount * 5 / 100)
    elif rating.casefold() == 'good':
            return math.ceil(amount * 10 / 100)
    elif rating.casefold() == 'great':
            return math.ceil(amount * 15 / 100)
    elif rating.casefold() == 'excellent':
            return math.ceil(amount * 20 / 100)
    else:
        return 'Rating not recognised'