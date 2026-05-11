# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

def array(string):
    lst = []
    new_str = ""
    lst = string.split(',')
    if len(lst) == 1 or len(lst) == 2:
        return None
    else:
        lst.pop(0)
        lst.pop(-1)
        for i in lst:
            new_str += i + " "
    return new_str.rstrip(" ")