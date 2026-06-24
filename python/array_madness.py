# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/train/python

def array_madness(a,b):
    listA = []
    listB = []
    for i in a:
        listA.append(i ** 2)
    for j in b:
        listB.append(j ** 3)
    return True if sum(listA) > sum(listB) else False