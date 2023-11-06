#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    intenger_maximum = my_list[0]
    for j in range(len(my_list)):
        if (my_list[j] > intenger_maximum):
            intenger_maximum = my_list[j]
    return intenger_maximum
