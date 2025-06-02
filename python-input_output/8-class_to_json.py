#!/usr/bin/python3

'''
This module contain 1 function
'''


def class_to_json(obj):
    '''
    function that returns the dictionary description with 
    simple data structure
    '''
    return obj.__dict__