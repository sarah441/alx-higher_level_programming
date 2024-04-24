#!/usr/bin/python3
"""
Creating my list to be sorted
"""


class MyList(list):
    """babyclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        self.sort()
        print(self)
