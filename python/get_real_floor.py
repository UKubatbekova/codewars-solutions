# https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python

def get_real_floor(n):
    if n == 1:
        return 0
    elif 2 <= n <= 12:
        return n-1
    elif n > 13:
        return n-2
    else:
        return n