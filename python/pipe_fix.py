# https://www.codewars.com/kata/56b29582461215098d00000f/train/python

def pipe_fix(nums):
    lst = []
    for n in range(nums[0], nums[-1] + 1):
        lst.append(n)
    return lst