#!/usr/bin/env python3

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]


def middle_number(n):
    s = str(n)
    length = len(s)
    mid = length // 2

    if length % 2 == 0:
        # even length - return middle two digits
        return s[mid-1:mid+1]
    else:
        # odd length
        if '.' in s:
            # Return middle char + next char for decimal numbers
            return s[mid:mid+2]
        else:
            return s[mid]

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]
