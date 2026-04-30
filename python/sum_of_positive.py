# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    sum_positive = []
    if len(arr) > 0:
        for i in arr:
            if i > 0:
                sum_positive.append(i)
        return sum(sum_positive)
    else:
        return 0