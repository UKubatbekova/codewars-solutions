# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

def solution(text, ending):
    length = len(ending)
    if text[-length:] == ending:
        return True
    else:
        return False