#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    the_list = []
    for j in range(0, list_length):
        try:
            d = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            d = 0
        except ZeroDivisionError:
            print("division by 0")
            d = 0
        except IndexError:
            print("out of range")
            d = 0
        finally:
            the_list.append(d)
    return (the_list)
