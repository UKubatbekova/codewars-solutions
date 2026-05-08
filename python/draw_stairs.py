# https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/python

def draw_stairs(n):
    result = ""
    for i in range(n):
        result += i * " " + "I" + "\n"
    return result.rstrip()