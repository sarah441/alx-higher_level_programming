#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dic = {}
    for n in a_dictionary:
        multi_dic[n] = a_dictionary[n] * 2
    return multi_dic
