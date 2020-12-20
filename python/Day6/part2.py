#!/usr/bin/env python3
from sys import stdin

count = 0
c = 0
yes = [0] * 26
for line in stdin:
    if line == "\n":
        count += yes.count(c)
        c = 0
        yes = [0] * 26
    else:
        c += 1
        for ch in line.strip():
            yes[ord(ch) - ord("a")] += 1

print(count)
