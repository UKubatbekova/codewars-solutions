# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

def find_needle(haystack):
    position = haystack.index('needle')
    if "needle" in haystack:
        return "found the needle at position " + str(position)