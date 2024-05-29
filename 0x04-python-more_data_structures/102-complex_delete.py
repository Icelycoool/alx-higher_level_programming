#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    removed_item = [key for key, val in a_dictionary.items() if val == value]
    for key in removed_item:
        del a_dictionary[key]
