# https://www.codewars.com/kata/5848cd33c3689be0dc00175c/train/python

def add(s1, s2):
    result = 0
    for i in s1:
        result += ord(i)
    for j in s2:
        result += ord(j)
    return result