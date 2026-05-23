# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python

def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year and abs(year_of_birth - current_year) == 1:
        return "You are " + str(abs(year_of_birth - current_year)) + " year old."
    elif year_of_birth < current_year:
        return "You are " + str(abs(year_of_birth - current_year)) + " years old."
    elif year_of_birth > current_year:
        if abs(year_of_birth - current_year == 1):
            return "You will be born in " + str(year_of_birth - current_year) + " year."
        else:
            return "You will be born in " + str(year_of_birth - current_year) + " years."
    else:
        return "You were born this very year!"