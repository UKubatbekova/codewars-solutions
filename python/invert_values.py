# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

def invert(lst):
    new_lst = []
    for i in lst:
        if i < 0:
            new_lst.append(abs(i))
        else:
            new_lst.append(-i)
    return new_lst