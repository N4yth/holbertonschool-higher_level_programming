#!/usr/bin/python3
i = 0
while (i < 9):
    j = i + 1
    while (j < 10):
        if (i == 8 and j == 9):
            break
        print("{}{}, ".format(i, j), end="")
        j += 1
    i += 1
print("{}{}".format(i - 1, j))
