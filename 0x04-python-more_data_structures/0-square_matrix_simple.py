#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    the_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        the_matrix.append(result)
    return the_matrix
