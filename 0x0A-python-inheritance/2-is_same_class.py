#!/usr/bin/python3
"""
to check if the type is the same 
"""


def is_same_class(obj, a_class):
    """return true if obj is same class a_class, if not false"""
    if (type(obj) == a_class):
        return True
    else:
        return False
