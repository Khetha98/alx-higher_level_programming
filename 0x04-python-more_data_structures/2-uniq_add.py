#!/usr/bin/python3
def uniq_add(my_list=[]):
    the_list = []
    k = 0
    for i in my_list:
        if i not in the_list:
            k += i
            the_list.append(i)
    return k
