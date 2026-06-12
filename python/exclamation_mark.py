# https://www.codewars.com/kata/57fae964d80daa229d000126/train/python

def remove(s):
    result = ""
    if len(s) > 0 and s[-1] == "!":
        result += s[:-1]
    else:
        result += s
    return result