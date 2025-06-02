#!/usr/bin/python3

'''
This module contain 1 function that append string in text
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    this function to append string in a file
    '''
    with open(filename, 'a', encoding='UTF-8') as fichier:
        return fichier.write(json.dumps(my_obj))
