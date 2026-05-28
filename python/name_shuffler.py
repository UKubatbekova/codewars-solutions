# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

def name_shuffler(str_):
    lst = str_.split(" ")
    result = lst[-1] + " " + lst[0]
    return result