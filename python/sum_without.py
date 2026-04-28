# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    lst = list(arr)
    lst.remove(max(lst))
    lst.remove(min(lst))
    return sum(lst)