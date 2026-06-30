# https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python

def fuel_price(litres, price_per_litre):
    discount = min((litres // 2) * 0.05, 0.25)
    total = litres * (price_per_litre - discount)
    return round(total, 2)