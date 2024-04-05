#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    max = 0
    max_k = 0
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            max_k = key
    return max_k

