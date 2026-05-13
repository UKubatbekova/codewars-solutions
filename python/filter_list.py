# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    lst = []
    for i in l:
        if isinstance(i, int):
            lst.append(i)
    return lst