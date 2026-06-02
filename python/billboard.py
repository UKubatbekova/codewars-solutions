# https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python

def billboard(name, price=30):
    total = 0
    for i in range(len(name)):
        total += price
    return total