#!/usr/bin/env python3
from sys import stdin

count = 0
for line in stdin:
    parts = line.split(" ")

    start, end = [int(i) - 1 for i in parts[0].split("-")]
    ch = parts[1][0]
    pwd = parts[2]

    if (pwd[start] == ch) ^ (pwd[end] == ch):
        count += 1

print(count)
