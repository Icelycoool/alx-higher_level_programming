#!/usr/bin/python30x04-python-more_data_structures
def search_replace(my_list, search, replace):
    output = [num if num != search else replace for num in my_list]
    return output
