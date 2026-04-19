# https://www.codewars.com/kata/5713bc89c82eff33c60009f7/train/python

def to_freud(sentence):
    lst = []
    result = ""
    lst = sentence.split(" ")
    if sentence == "sex" or len(sentence) == 0:
        return result
    for i in range(len(lst)):
        result += "sex "
    return result.rstrip()