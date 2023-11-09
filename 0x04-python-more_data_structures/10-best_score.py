#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        the_list = list(a_dictionary.keys())
        l = ""
        s = 0
        for i in the_list:
            if a_dictionary[i] > s:
                s = a_dictionary[i]
                l = i
        return l
