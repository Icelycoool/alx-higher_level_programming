#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_num = 0
    total_value = 0

    for char in roman_string[::-1]:
        value = roman_nums.get(char, 0)
        if value >= prev_num:
            total_value += value
        else:
            total_value -= value
        prev_num = value
    return total_value
