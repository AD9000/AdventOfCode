#!/usr/bin/env python3
from sys import stdin

count = 0
for line in stdin:
    parts = line.split(" ")

    start, end = map(int, parts[0].split("-"))
    ch = parts[1][0]
    pwd = parts[2]

    c = pwd.count(ch)
    if c <= end and c >= start:
        count += 1

print(count)
