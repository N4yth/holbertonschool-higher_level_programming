#!/usr/bin/python3

'''
This module contain 1 function for read a file
'''


def read_file(filename=""):
    '''
    this function read and print a file
    '''
    with open(filename, 'r', encoding='UTF-8') as fichier:
        print(fichier.read(), end="")
