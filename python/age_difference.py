# https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/python

def difference_in_ages(ages):
    max_age = max(ages)
    min_age = min(ages)
    difference = (min_age, max_age, max_age - min_age)
    return difference