#!/usr/bin/python3
from sys import argv


def main():
    pass


if __name__ == "__main__":
    args = argv[1:]
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument:")
        print("1 : {}".format(args[0]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(0, len(argv) - 1):
            print("{}: {}".format(i + 1, args[i]))
