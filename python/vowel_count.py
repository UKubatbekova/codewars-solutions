# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    total = 0
    for i in sentence:
        if i in "aeiou":
            total += 1
    return total