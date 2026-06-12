# https://www.codewars.com/kata/65128d27a5de2b3539408d83/train/python

import heapq

def win_round(you, opp):
    your_num = ""
    opp_num = ""
    for i in heapq.nlargest(2, you):
        your_num += str(i)
    for j in heapq.nlargest(2, opp):
        opp_num += str(j)
    return True if int(your_num) > int(opp_num) else False