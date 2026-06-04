# https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    result = ""
    if len(a) > len(b):
        result += b + a + b
    else:
        result += a + b + a
    return result