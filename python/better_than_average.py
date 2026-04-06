# https://www.codewars.com/kata/5601409514fc93442500010b

def better_than_average(class_points, your_points):
    avg = (sum(class_points) + your_points) / (len(class_points) + 1)
    if avg < your_points:
        return True
    else:
        return False