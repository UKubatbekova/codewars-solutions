# https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    result = ""
    for i in string:
        if i.isalpha() and i.islower():
            result += i.upper()
        elif i.isalpha() and i.isupper():
            result += i.lower()
        elif i.isdigit():
            result += i
        else:
            result += i
    return result