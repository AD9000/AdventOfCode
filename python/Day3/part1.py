#!/usr/bin/env python3
from sys import stdin

columns = len(input())
col = 3
count = 0

for line in stdin:
    if line[col] == "#":
        count += 1

    col = (col + 3) % columns

print(count)
