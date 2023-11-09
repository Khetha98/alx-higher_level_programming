#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        d = 0
        for i in my_list:
            n += (i[0] * i[1])
            d += (i[1])
        return (n/d)
    return 0
