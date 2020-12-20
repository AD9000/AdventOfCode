#!/usr/bin/env python3
from sys import stdin

inst = [list(i.strip().split(" ")) for i in stdin]

l = len(inst)
check = [False] * l

curr = 0
acc = 0
while True:
    if check[curr]:
        break

    lastInst = 0
    check[curr] = True
    if inst[curr][0] == "jmp":
        curr += int(inst[curr][1])
    elif inst[curr][0] == "nop":
        curr += 1
    else:
        acc += int(inst[curr][1])
        curr += 1

print(acc)
