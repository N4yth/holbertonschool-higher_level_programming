#!/usr/bin/python3
import sys

args = sys.argv[1:]
if (len(args) == 0):
    print("0 arguments.")
elif (len(args) == 1):
    print("1 argument:")
    print("1 : {}".format(args[0]))
else:
    print("{} argument:".format(len(args)))
    for i in range(0, len(args)):
        print("{} :{}".format(i + 1, args[i]))
