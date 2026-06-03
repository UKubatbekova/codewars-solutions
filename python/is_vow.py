# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

def is_vow(inp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = []
    for i in inp:
        if chr(i) in vowels:
            lst.append(chr(i))
        else:
            lst.append(i)
    return lst