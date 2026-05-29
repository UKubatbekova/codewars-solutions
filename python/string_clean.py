# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

def string_clean(s):
    result = ""
    for i in s:
        if i.isdigit():
            result += i.replace(i, "")
        else:
            result += i
    return result