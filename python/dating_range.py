# https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python

def dating_range(age):
    if age > 14:
        min_age = age / 2 + 7
        max_age = 2 * (age - 7)
    else:
        min_age = age - 0.10 * age
        max_age = age + 0.10 * age
    return f"{int(min_age)}-{int(max_age)}"