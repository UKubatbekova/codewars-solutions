# https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python

def lowercase_count(strng):
    counter = 0
    for i in strng:
        if i.islower():
            counter += 1
    return counter