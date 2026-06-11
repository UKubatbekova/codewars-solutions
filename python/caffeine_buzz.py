# https://www.codewars.com/kata/5434283682b0fdb0420000e6/train/python

def caffeine_buzz(n):
    result = ""
    if n % 3 == 0 and n % 4 == 0:
        result = "Coffee"
        if (n % 3 == 0 and n % 4 == 0) and (n % 2 == 0):
            result += "Script"
    elif n % 3 == 0:
        result = "Java"
        if n % 3 == 0 and n % 2 == 0:
            result += "Script"
    else:
        return "mocha_missing!"
    return result