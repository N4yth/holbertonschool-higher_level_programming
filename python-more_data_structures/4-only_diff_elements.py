#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    common = []
    for element_set_1 in set_1:
        if (element_set_1 not in set_2):
            common.append(element_set_1)
    for element_set_2 in set_2:
        if (element_set_2 not in set_1):
            common.append(element_set_2)
    return (common)
