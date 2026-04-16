# https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/python

def weather_info (temp):
    celsius = (temp - 32) * (5/9)
    if (celsius > 0):
        return (str(celsius) + " is above freezing temperature")
    else:
        return (str(celsius) + " is freezing temperature")