# https://www.codewars.com/kata/578a8a01e9fd1549e50001f1/train/python

def period_is_late(last,today,cycle_length):
    difference = (today - last)
    if difference.days > cycle_length:
        return True
    else:
        return False