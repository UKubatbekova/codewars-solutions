# https://www.codewars.com/kata/56c22c5ae8b139416c00175d

def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Missing necessary information")
    result = candidate['min_salary'] - (candidate['min_salary'] * 0.1)
    if result <= job['max_salary']:
        return True
    else:
        return False