# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python

import re

def validate_usr(username):
    pattern = r"[a-z_0-9]{4,16}"
    return True if re.fullmatch(pattern, username) else False