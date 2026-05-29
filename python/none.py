# https://www.codewars.com/kata/545993ee52756d98ca0010e1/train/python

def none(lst, func):
    for i in lst:
        if func(i) == True:
            return False
    return True