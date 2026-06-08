# https://www.codewars.com/kata/563d59dd8e47a5ed220000ba/train/python

def get_sum_of_digits(num):
    total = 0
    lst = []
    for i in str(num):
        lst.append(i)
        total += int(i)
    return total