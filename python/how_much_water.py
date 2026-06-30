# https://www.codewars.com/kata/575fa9afee048b293e000287/train/python

def how_much_water(water, load, clothes):
    water_needed = water * (1.1 ** (clothes - load))
    if clothes < load:
        return "Not enough clothes"
    elif clothes > 2 * load:
        return "Too much clothes"
    else:
        return round(water_needed, 2)