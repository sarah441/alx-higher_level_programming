#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    i = number % 10
    print("{}".format(i), end="")
    return(i)
