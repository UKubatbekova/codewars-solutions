# https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python

def sp_eng(sentence): 
    search = "english"
    return True if search.casefold() in sentence.casefold() else False