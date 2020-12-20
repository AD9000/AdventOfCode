#!/usr/bin/env python3
from sys import stdin
import re


def checkNum(num, low, high):
    return (int(num) >= low and int(num) <= high) if num.isnumeric() else False


# validate params
def validate(inf):
    params = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # existence
    for key in params:
        if key not in inf:
            return False

    check = True
    # byr
    # print(inf)
    check = check and checkNum(inf["byr"], 1920, 2002)
    check = check and checkNum(inf["iyr"], 2010, 2020)
    check = check and checkNum(inf["eyr"], 2020, 2030)

    hgt = inf["hgt"]
    hsuf = hgt[-2:]
    if not hgt[:-2].isnumeric():
        return False

    hnum = int(hgt[:-2])

    if hsuf == "in":
        check = check and (hnum >= 59 and hnum <= 76)
    elif hsuf == "cm":
        check = check and (hnum >= 150 and hnum <= 193)
    else:
        return False

    check = check and bool(re.match("^#[a-z0-9]{6}$", inf["hcl"]))

    check = check and (
        inf["ecl"] in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    )

    check = check and bool(re.match("^[0-9]{9}$", inf["pid"]))

    return check


count = 0
info = {}
for line in stdin:
    # reset
    if line == "\n":
        count += 1 if validate(info) else 0
        info = {}
    else:
        for param in line.split(" "):
            k, v = map(str.strip, param.split(":"))
            info[k] = v

if info:
    print(count + validate(info))
else:
    print(count)
