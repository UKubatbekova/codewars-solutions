# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):
    result = weight / height ** 2
    if result <= 18.5:
        return "Underweight"
    elif result <= 25.0:
        return "Normal"
    elif result <= 30.0:
        return "Overweight"
    elif result > 30:
        return "Obese"