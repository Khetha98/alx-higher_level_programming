#!/usr/bin/python3
"""This module defines the Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of the size n
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        tri = t[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        t.append(tmp)
    return t
