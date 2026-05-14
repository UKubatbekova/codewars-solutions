# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python

def who_is_paying(name):
    lst = []
    if len(name) == 0:
        lst.append(name)
    elif len(name) == 1 or len(name) == 2:
        lst.append(name)
    else:
        lst.append(name)
        lst.append(name[0] + name[1])
    return lst