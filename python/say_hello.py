# https://www.codewars.com/kata/5302d846be2a9189af0001e4/train/python

def say_hello(name, city, state):
    result = "Hello, "
    for i in name:
        result += i + " "
    return result.rstrip() + "! Welcome to " + city + ", " + state + "!"