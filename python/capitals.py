# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

def capitals(word):
    lst = []
    for i in range(len(word)):
        if word[i].isupper():
            lst.append(i)
    return lst