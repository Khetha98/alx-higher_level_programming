#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if (idx < 0 or idx >= len(my_list)):
            return my_list
        else:
            another_list = my_list.copy()
            another_list[idx] = element
            return another_list
