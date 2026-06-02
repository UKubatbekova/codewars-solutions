# https://www.codewars.com/kata/59811fd8a070625d4c000013/train/python

def integrate(coefficient, exponent):
    result = coefficient // (exponent + 1)
    return str(result) + "x^" + str(exponent + 1)