# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python

def replace_exclamation(st):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for i in st:
        if i in vowel:
            result += "!"
        else:
            result += i
    return result