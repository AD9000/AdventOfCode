#!/usr/bin/env python3
from sys import stdin

# check params
def check(inf):
    params = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in params:
        if key not in inf:
            return False
    return True


count = 0
info = {}
for line in stdin:
    # reset
    if line == "\n":
        count += 1 if check(info) else 0
        info = {}
    else:
        for param in line.split(" "):
            k, v = param.split(":")
            info[k] = v

if info:
    print(count + check(info))
else:
    print(count)
