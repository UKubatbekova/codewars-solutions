# https://www.codewars.com/kata/5708f682c69b48047b000e07/train/python

def multiply(n):
    length = 0
    for i in str(n):
        if i.isdigit():
            length += 1
    return n * 5 ** length    