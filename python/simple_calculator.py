# https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python

def calculator(x, y, op):
    if isinstance(x, int) and isinstance(y, int) and op == '+':
        return x + y
    elif isinstance(x, int) and isinstance(y, int) and op == '-':
        return x - y
    elif isinstance(x, int) and isinstance(y, int) and op == '*':
        return x * y
    elif isinstance(x, int) and isinstance(y, int) and op == '/':
        return x / y
    else:
        return 'unknown value'