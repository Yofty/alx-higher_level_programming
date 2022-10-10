#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            y += 1
        except (ValueError, TypeError):
            continue
    print("")
    return y
