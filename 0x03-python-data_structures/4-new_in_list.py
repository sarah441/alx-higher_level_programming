#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    n = len(my_list) - 1
    if idx < 0 or idx > n:
        return my_list
    else:
        newlist[idx] = element
        return newlist
