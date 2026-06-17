# https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python

import re

def validate_code(code):
    pattern = r"^[1-3]"
    return bool(re.match(pattern, str(code)))