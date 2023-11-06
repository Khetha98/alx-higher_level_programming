#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    the_list = []
    for j in my_list:
        if (j % 2 == 0):
            the_list.append(True)
        else:
            the_list.append(False)
    return the_list
