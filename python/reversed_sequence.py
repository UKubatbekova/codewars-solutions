# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def reverse_seq(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(i)
    lst.sort(reverse=True)
    return lst