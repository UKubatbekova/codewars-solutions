# https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python

def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst