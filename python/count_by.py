# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

def count_by(x, n):
    lst = []
    for i in range(1, n + 1):
        lst.append(i * x)
    return lst