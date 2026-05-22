# https://www.codewars.com/kata/5a05fe8a06d5b6208e00010b/train/python

def seq_to_one(n):
    lst = []
    if n <= 0:
        for i in range(n, 2, 1):
            lst.append(i)
    else:
        for i in range(n, 0, -1):
            lst.append(i)
    return lst