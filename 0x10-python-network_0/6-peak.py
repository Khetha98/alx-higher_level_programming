#!/usr/bin/python3
""" It Finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: returns peak of list_of_integers or None
    """
    s = len(list_of_integers)
    mid_e = s
    mid = s // 2

    if s == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < s - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_integers[mid]
