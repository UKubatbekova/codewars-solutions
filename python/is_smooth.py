# https://www.codewars.com/kata/5886d35d4703f125a6000008/train/python

def is_smooth(arr):
    if arr[0] != arr[-1]:
        return False
    elif len(arr) % 2 != 0:
        mid = len(arr) // 2
        return True if arr[mid] == arr[0] else False
    else:
        mid1 = len(arr) // 2
        mid2 = len(arr) // 2 -1
        res = arr[mid1] + arr[mid2]
        return True if res == arr[0] else False