#!/usr/bin/python3
for i in range(100):
    digit = i // 10
    mod = i % 10
    if digit < mod:
        if i == 89:
            print("{:02}".format(i))
        else:
            print("{:02}, ".format(i), end="")
