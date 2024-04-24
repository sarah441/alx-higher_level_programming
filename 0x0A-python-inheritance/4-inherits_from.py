#!/usr/bin/python3
'''Method'''


def inherits_from(obj, a_class):
    '''Determine if they are inherited but not the same idk why tbh'''
    return isinstance(obj, a_class) and type(obj) != a_class
