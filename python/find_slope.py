# https://www.codewars.com/kata/55a75e2d0803fea18f00009d/train/python

def find_slope(points):
    if points[2] - points[0] == 0:
        return "undefined"
    else:
        result = (points[3] - points[1]) / (points[2] - points[0])
        return str(int(result)) if result == int(result) else str(result)