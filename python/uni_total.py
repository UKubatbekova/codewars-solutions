# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python

def uni_total(s):
    counter = 0
    for i in s:
        counter += ord(i)
    return counter