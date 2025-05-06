#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    pass


if __name__ == "__main__":
    a = 10
    b = 5
    resu = add(a, b)
    print("{} + {} = {}".format(a, b, resu))
    resu = sub(a, b)
    print("{} - {} = {}".format(a, b, resu))
    resu = mul(a, b)
    print("{} * {} = {}".format(a, b, resu))
    resu = div(a, b)
    print("{} / {} = {}".format(a, b, resu))
