# https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

def combat(health, damage):
    new_health = health - damage
    return new_health if new_health > 0 else 0