#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = [[x ** 2 for x in y] for y in matrix]
    return my_new_matrix
