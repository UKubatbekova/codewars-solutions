# https://www.codewars.com/kata/56d5166ec87df55dbe000063/train/python

def sum_average(lists: list[list[int]]) -> float:
    lst = []
    for i in range(len(lists)):
        lst.append(sum(lists[i]) / len(lists[i]))
    return sum(lst)