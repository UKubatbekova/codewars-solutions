# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

def multi_table(number):
    result = ""
    for i in range(1, 11):
        multiplication = i * number
        result += str(i) + " * " + str(number) + " = " + str(multiplication) + "\n"
    return result.rstrip("\n")