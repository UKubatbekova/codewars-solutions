# https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python

def html_special_chars(data): 
    result = ""
    for i in data:
        if i == "<":
            result += "&lt;"
        elif i == ">":
            result += "&gt;"
        elif i == '"':
            result += "&quot;"
        elif i == "&":
            result += "&amp;"
        else:
            result += i
    return result