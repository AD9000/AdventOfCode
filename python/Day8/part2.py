#!/usr/bin/env python3
from sys import stdin

inst = [list(i.strip().split(" ")) for i in stdin]


def runCheck():
    l = len(inst)
    check = [False] * l

    curr = 0
    acc = 0
    while True:
        if curr >= l:
            return acc
        if check[curr]:
            return None

        lastInst = 0
        check[curr] = True
        if inst[curr][0] == "jmp":
            curr += int(inst[curr][1])
        elif inst[curr][0] == "nop":
            curr += 1
        else:
            acc += int(inst[curr][1])
            curr += 1


c = 0
for i in inst:
    if i[0] == "jmp":
        i[0] = "nop"
        ans = runCheck()
        if ans:
            print(ans)
            break
        else:
            i[0] = "jmp"
    elif i[0] == "nop":
        i[0] = "jmp"
        ans = runCheck()
        if ans:
            print(ans)
            break
        else:
            i[0] = "nop"
