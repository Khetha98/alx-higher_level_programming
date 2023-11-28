#!/usr/bin/python3

"""

The module defines the matrix division function

"""


def matrix_divided(matrix, div):
    """The function divides all elements of a matrix by the given number

    Args:
        matrix: A list of lists (matrix)
        div: Number to be used for the division
    Raises:
        TypeError: If a matrix contains no numbers
        TypeError: If a matrix contains rows wit different sizes
        TypeError: If div is not the int or float
        ZeroDivisionError: If div is equal to 0
    Returns:
        A new matrix which represents a result of divisions
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
