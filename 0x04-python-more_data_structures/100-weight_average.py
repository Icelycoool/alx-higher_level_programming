#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_nums = 0
    total_weight = 0

    for score, weight in my_list:
        total_weight += score * weight
        weighted_nums += weight

    return total_weight / weighted_nums
