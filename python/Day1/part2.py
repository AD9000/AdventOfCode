#!/usr/bin/env python3
from sys import stdin


def sum3(sum2, index):
    s = set([])

    j = 0
    for num in nums:
        if j == index:
            continue
        j += 1

        if (sum2 - num) in s:
            return num * (sum2 - num)
        else:
            s.add(num)

    return 0


nums = [int(l[:-1]) for l in stdin]
sums = []

i = 0
for num in nums:
    sm = sum3(2020 - num, i)

    if sm > 0:
        print(sm * num)
        break

    i += 1
