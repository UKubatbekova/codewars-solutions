# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

def even_last(numbers):
    result = 0
    if len(numbers) == 0:
        return 0
    else:
        for n in range(len(numbers)):
            if n % 2 == 0:
                result += numbers[n]
    return result * numbers[-1]