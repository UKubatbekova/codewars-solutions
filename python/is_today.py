# https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python

from datetime import datetime

def is_today(date : datetime) -> bool:
    if date.year == datetime.today().year and date.month == datetime.today().month and date.day == datetime.today().day:
        return True
    else:
        return False