# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
    result = []
    for i in str(n):
        result.append(int(i))
    result.reverse()
    return result