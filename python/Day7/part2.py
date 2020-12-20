#!/usr/bin/env python3
from sys import stdin
from collections import deque

mapper = {}
# m2 = {}
values = {}
bgs = []

uid = 0
for line in stdin:
    line = line.strip()
    # container, bags
    container, bags = line.split(" contain ")

    container = container.split(" bag")[0]
    cnum = -1
    if container in mapper:
        cnum = mapper[container]
    else:
        mapper[container] = uid
        cnum = uid
        bgs.append(set([]))
        uid += 1

    m2[cnum] = container

    # handling the bags
    bags = bags.split(", ")
    for bag in bags:
        bag = bag.split(" bag")[0]
        # since there are no 2 digit nums...
        bcount = 0
        if bag.strip() == "no other":
            print(bag)
            bag = "other"
            bcount = 0
        else:
            bcount = int(bag[0])
            bag = bag[2:].strip()

        bnum = -1
        if bag in mapper:
            bnum = mapper[bag]
        else:
            mapper[bag] = uid
            bnum = uid
            bgs.append(set([]))
            uid += 1

        if cnum not in values:
            values[cnum] = {}

        # bgs[bnum].add(cnum)
        bgs[cnum].add(bnum)
        values[cnum][bnum] = bcount
        # m2[bnum] = bag

cache = {mapper["other"]: 0}


def findVal(curr):
    # print(curr, m2[curr])
    if curr in cache.keys():
        return cache[curr]
    else:
        val = 0
        for i in bgs[curr]:
            val += findVal(i) * values[curr][i] + values[curr][i]
        cache[curr] = val
        return val


print(findVal(mapper["shiny gold"]))
