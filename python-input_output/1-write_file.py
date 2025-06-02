#!/usr/bin/python3

'''
This module contain 1 function tat write string in text
'''


def write_file(filename="", text=""):
    '''
    this function read and print a file
    '''
    with open(filename, 'w', encoding='UTF-8') as fichier:
        return fichier.write(text)
