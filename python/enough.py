# https://www.codewars.com/kata/5875b200d520904a04000003/train/python

def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    else:
        res = cap - on
    return abs(res - wait)