#!/usr/bin/python3
def no_c(my_string):
    str_to_update = ""
    for j in my_string:
        if j != "c" and j != "C":
            str_to_update += j
    return str_to_update
