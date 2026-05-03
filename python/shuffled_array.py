# https://www.codewars.com/kata/589573e3f0902e8919000109/train/python

def shuffled_array(s):
    total = sum(s)
    for i in s:
        if i == total - i:
            s.remove(i)
            break
    return sorted(s)