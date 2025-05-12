#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    tmp_old_i = "M" #put the highest letter possible to prevent to enter in the if on the first itereation
    if (roman_string is None or type(roman_string) != str):
        return (0)
    data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in roman_string:
        if (data[i] > data[tmp_old_i]):
            result += data[i] - data[tmp_old_i] * 2
        else:
            result += data[i]
        tmp_old_i = i
    return (result)
