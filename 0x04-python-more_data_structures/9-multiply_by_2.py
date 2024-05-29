#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = a_dictionary.copy()
    for key in multiplied_dict.keys():
        multiplied_dict[key] *= 2
    return multiplied_dict

