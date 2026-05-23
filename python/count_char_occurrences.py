# https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

def count_char_occurrences(strng, char):
    counter = 0
    for i in strng:
        if i == char:
            counter += 1
    return counter