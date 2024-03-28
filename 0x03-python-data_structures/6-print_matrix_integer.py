#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in r:
            print("{:d}".format(c), sep='', end='')
            if (c != r[len(r) - 1]):
                print(' ', end='')
        print()
