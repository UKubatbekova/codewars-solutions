# https://www.codewars.com/kata/5704aea738428f4d30000914/train/python

def triple_trouble(one, two, three):
    res = ""
    length = len(one)
    for i in range(length):
        res += one[i] + two[i] + three[i]
    return res