# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

def sum_mul(n, m):
    lst = []
    if n > 0 and m > 0:
        for i in range(n, m, n):
            lst.append(i)
        return sum(lst)
    else:
        return 'INVALID'