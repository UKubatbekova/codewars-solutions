# https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python

def sorter(textbooks):
    textbooks.sort(key=str.casefold)
    return textbooks