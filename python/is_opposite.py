# https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7/train/python

def is_opposite(s1,s2):
    if len(s1) == 0 and len(s2) == 0:
        return False
    elif s1.swapcase() == s2 and s2.swapcase() == s1:
        return True
    else:
        return False