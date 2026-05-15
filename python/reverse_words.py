# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    lst = []
    result = ""
    lst += s.split(" ")
    lst.reverse()
    for i in lst:
        result += i + " "
    return result.rstrip()