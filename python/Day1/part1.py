#!/usr/bin/env python3
from sys import stdin

s = set([])
for line in stdin:
    num = int(line[:-1])
    if (2020 - num) in s:
        print(num * (2020 - num))
        break
    else:
        s.add(num)
