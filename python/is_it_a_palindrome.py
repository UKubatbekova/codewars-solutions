# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

def is_palindrome(s):
    return True if s[0:].lower() == s[::-1].lower() else False