#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    score = -1
    for i in a_dictionary:
        if (a_dictionary[i] > score):
            score = a_dictionary[i]
            biggest = i
    if (score == -1):
        return (None)
    return (biggest)
