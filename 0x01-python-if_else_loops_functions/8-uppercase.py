#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
            print("{}".format(upper_char), end="")
        else:
            print("{}".format(char), end="")
    print()
