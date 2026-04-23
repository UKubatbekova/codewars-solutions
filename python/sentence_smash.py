# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

def smash(words):
    sentence = ''
    for i in words:
        sentence += i + " "
    return sentence.rstrip()