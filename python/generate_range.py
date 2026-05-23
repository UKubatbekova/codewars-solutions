# https://www.codewars.com/kata/55eca815d0d20962e1000106/train/python

def generate_range(start, stop, step):
    lst = []
    for i in range(start, stop + 1, step):
        lst.append(i)
    return lst