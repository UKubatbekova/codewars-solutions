# https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/train/python

def get_status(is_busy):
    status = {}
    if is_busy is True:
        status['status'] = 'busy'
        return status
    else:
        status['status'] = 'available'
        return status