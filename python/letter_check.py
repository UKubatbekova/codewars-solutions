# https://www.codewars.com/kata/57470efebf81fea166001627/train/python

def letter_check(string_pair: list[str]) -> bool: 
    for i in string_pair[1].casefold():
        if i not in string_pair[0].casefold():
            return False
    return True