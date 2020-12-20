#!/usr/bin/env python3
from sys import stdin


def getRowVal(p):
    l, r = 0, 128
    for i in range(7):
        mid = (l + r) // 2
        if p[i] == "F":
            r = mid
        else:
            l = mid

    return l


def getColVal(p):
    l, r = 0, 8
    for i in range(7, 10):
        mid = (l + r) // 2
        if p[i] == "L":
            r = mid
        else:
            l = mid

    return l


def getVal(p):
    return (getRowVal(p) * 8) + getColVal(p)


# needs atleast 1-15 seats before and 1-15 seats to be empty
# note: this function doesn't care about immediate rows
# but that is enough for this input
def find(mx):
    up = mx - mx % 8 + 8
    lastAbs = None
    currAbs = None
    for i in range(0, up, 8):
        check = True
        for j in range(7):
            if (i + j) not in seats:
                # add into last abs or currAbs if needed
                if lastAbs is None:
                    lastAbs = i + j
                elif currAbs is None:
                    currAbs = i + j

                else:
                    if currAbs - lastAbs > 8 and (i + j) - currAbs > 8:
                        return currAbs
                    else:
                        lastAbs, currAbs = currAbs, i + j

                break

    if currAbs is None:
        return lastAbs
    elif currAbs - lastAbs > 8:
        return currAbs


seats = set([getVal(line.strip()) for line in stdin.readlines()])

# would be same as solving part 1, but micro-optimizations?? :P
# print(max(seats))

mx = max(seats)
print(find(mx))
