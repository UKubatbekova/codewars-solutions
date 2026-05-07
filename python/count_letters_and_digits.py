# https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

def count_letters_and_digits(s):
    counter = 0
    for i in s:
        if i.isdigit() or i.isalpha():
            counter += 1
    return counter