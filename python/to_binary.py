# https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/python

def to_binary(n):
    result = bin(n)
    return int(result[2:])