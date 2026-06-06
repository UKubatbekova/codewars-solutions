# https://www.codewars.com/kata/56368f37d464c0a43c00007f/train/python

def calculate(a, o, b):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        if b == 0:
            return None
        else:
            return a / b
    else:
        return None