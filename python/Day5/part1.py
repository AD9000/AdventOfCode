#!/usr/bin/env python3
from sys import stdin

"""
multiplying by 8 makes 
rows and columns independent
"sort" by columns and then rows
"""


def customMax(a, b):
    # row compare
    for i in range(7):
        if a[i] > b[i]:  # f > b
            return b
        elif b[i] > a[i]:
            return a

    # equal. Column compare
    for i in range(7, 10):
        if a[i] > b[i]:  # r > l
            return a
        elif b[i] > a[i]:
            return b

    # equal
    return a


def getVal(p):
    l, r = 0, 128
    val = None
    for i in range(6):
        mid = (l + r) // 2
        if p[i] == "F":
            r = mid
        else:
            l = mid

    val = l

    l, r = 0, 8
    for i in range(7, 9):
        mid = (l + r) // 2
        if p[i] == "L":
            r = mid
        else:
            l = mid

    return (val * 8) + l


# "sorting" by rows -> F = 0, B = 1
mx = input()
# print(getVal(mx))
for i in stdin:
    mx = customMax(mx, i.strip())

print(mx, getVal(mx))
