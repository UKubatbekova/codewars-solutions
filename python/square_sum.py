# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    squares = []
    for i in numbers:
        squares.append(i ** 2)
    return sum(squares)