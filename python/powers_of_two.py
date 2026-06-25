# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python

def powers_of_two(n):
    lst = []
    for i in range(0, n + 1):
        lst.append(2 ** i)
    return lst