# https://www.codewars.com/kata/55a996e0e8520afab9000055

def cookie(x):
    if isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    elif isinstance(x, (int, float)):
        return "Who ate the last cookie? It was Monica!"
    elif isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"