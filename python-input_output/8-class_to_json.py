#!/usr/bin/python3

'''
This module contain 1 function
'''
import json


def class_to_json(obj):
    '''
    function that returns the dictionary description with 
    simple data structure
    '''
    return json.loads(json.dumps(obj.__dict__))
