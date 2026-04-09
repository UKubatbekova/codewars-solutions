# https://www.codewars.com/kata/5865918c6b569962950002a1/train/python

def str_count(strng, letter):
    if letter in strng:
        return strng.count(letter)
    else:
        return 0