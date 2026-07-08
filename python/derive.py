# https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

def derive(coefficient, exponent): 
    result = coefficient * exponent
    if exponent == 2:
        return str(result) + "x^" + str(exponent)
    else:
        return str(result) + "x^" + str(exponent - 1)