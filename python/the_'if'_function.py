# https://www.codewars.com/kata/54147087d5c2ebe4f1000805

from collections.abc import Callable

def _if(bool, func1: Callable, func2: Callable):
    if bool:
        return func1()
    else:
        return func2()