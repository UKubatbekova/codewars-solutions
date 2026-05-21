# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    lst = []
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            lst.append(i)
    else:
        for i in range(a, b + 1):
            lst.append(i)
    return sum(lst)