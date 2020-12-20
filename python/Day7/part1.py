#!/usr/bin/env python3
from sys import stdin
from collections import deque

mapper = {}
# m2 = {}
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

    # m2[cnum] = container

    # handling the bags
    bags = bags.split(", ")
    for bag in bags:
        bag = bag.split(" bag")[0]
        # since there are no 2 digit nums...
        bag = bag[2:]
        if bag.strip() == "other":
            continue
        bnum = -1
        if bag in mapper:
            bnum = mapper[bag]
        else:
            mapper[bag] = uid
            bnum = uid
            bgs.append(set([]))
            uid += 1

        # bgs[bnum].add(cnum)
        bgs[bnum].add(cnum)

        # m2[bnum] = bag


# building the graph
allb = set(range(uid))

q = deque([mapper["shiny gold"]])
count = -1
while len(q) > 0:
    current = q.popleft()

    if current not in allb:
        continue

    count += 1

    # look at all parents
    allb.remove(current)
    # print(current, m2[current])

    for i in bgs[current]:
        q.append(i)

print(count)


# print(bgs)
