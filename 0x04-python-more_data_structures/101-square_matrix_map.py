#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda y: list(map(lambda o: o ** 2, y)), matrix))
