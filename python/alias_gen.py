# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    if f_name[0].isalpha() and l_name[0].isalpha():
        return FIRST_NAME[f_name[0].upper()] + " " + SURNAME[l_name[0].upper()]
    else:
        return "Your name must start with a letter from A - Z."