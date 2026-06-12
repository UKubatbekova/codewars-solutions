# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    indexOfSpace = name.index(" ")
    return name[0].upper() + "." + name[indexOfSpace + 1].upper()