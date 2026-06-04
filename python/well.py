# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

def well(x):
    if x.count("good") == 1 or x.count("good") == 2:
        return "Publish!"
    elif x.count("good") > 2:
        return "I smell a series!"
    else:
        return "Fail!"