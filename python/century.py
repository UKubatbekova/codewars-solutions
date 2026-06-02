# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
    if year % 100 == 0:
        result = year // 100
    else:
        result = year // 100 + 1
    return result