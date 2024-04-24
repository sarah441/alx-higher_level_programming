#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a baby class of list"""
    def __init__(self):
        """construct"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
