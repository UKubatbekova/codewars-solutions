# https://www.codewars.com/kata/56f7493f5d7c12d1690000b6/train/python

def mean(lst):
    nums = []
    string = ""
    for i in lst:
        if i.isdigit():
            nums.append(int(i))
        else:
            string += i
    return [sum(nums) / 10, string]