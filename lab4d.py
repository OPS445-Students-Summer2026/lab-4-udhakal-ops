#!/usr/bin/env python3

def first_five(text):
    return text[:5]

def last_seven(text):
    return text[-7:]

def middle_number(number):
    text = str(number)

    if len(text) % 2 == 0:
        middle = len(text) // 2
        return text[middle - 1:middle + 1]
    else:
        middle = len(text) // 2
        return text[middle:middle + 2]

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]


if __name__ == "__main__":
    pass
