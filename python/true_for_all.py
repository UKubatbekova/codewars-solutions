# https://www.codewars.com/kata/54598d1fcbae2ae05200112c/train/python

def _all(seq, fun): 
    for s in seq:
        if fun(s) == False:
            return False
    return True