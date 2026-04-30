# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    first_year = 15
    second_year = 9
    cat_after_that = 4
    dog_after_that = 5
    if human_years == 1:
        return [human_years, first_year, first_year]
    else:
        dif = human_years - 2
        res = first_year + second_year
        return [human_years, (dif * cat_after_that) + res, (dif * dog_after_that) + res]