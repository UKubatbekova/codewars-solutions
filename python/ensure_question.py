# https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python

def ensure_question(s):
    if len(s) == 0 or s[-1] != "?":
        s += "?"
        return s
    else:
        return s