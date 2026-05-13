# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

def solve(s):
    lowercase = 0
    uppercase = 0
    for i in s:
        if i.islower():
            lowercase += 1
        else:
            uppercase += 1
    return s.lower() if lowercase == uppercase or lowercase > uppercase else s.upper()