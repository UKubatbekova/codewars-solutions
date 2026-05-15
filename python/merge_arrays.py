# https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python

def merge_arrays(arr1, arr2):
    result = []
    for i in arr1:
        if i not in result:
            result.append(i)
    for j in arr2:
        if j not in result:
            result.append(j)
    return sorted(result)