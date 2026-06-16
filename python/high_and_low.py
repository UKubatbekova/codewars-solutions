# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    lst = []
    for i in numbers.split(" "):
        lst.append(int(i))
    return f"{str(max(lst))} {str(min(lst))}"