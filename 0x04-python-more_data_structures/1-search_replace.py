#!/usr/bin/python3
def search_replace(my_list, search, replace):
    the_list = []
    for i in my_list:
        if i == search:
            the_list.append(replace)
        else:
            the_list.append(i)
    return the_list
