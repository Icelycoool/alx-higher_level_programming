#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1,10):
        if i != j:
            if i != 0 or j != 1:
                print("{:d}{:d}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
