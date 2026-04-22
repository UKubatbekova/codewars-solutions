# https://www.codewars.com/kata/67b7a527c9f842fd3b02adb8/train/python

def travel_distance(avg_speed, travel_time):
    travel_hours = travel_time / 60
    travel_kms = (avg_speed  * 1.852) * travel_hours
    return travel_kms