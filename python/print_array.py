# https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/python

def print_array(arr):
    result = ""
    for i in arr:
        result += str(i) + ","
    return result[:-1]