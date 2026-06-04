# https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python

def reverse(st):
    result = ""
    lst = st.split(" ")
    lst.reverse()
    result = " ".join(lst)
    return result