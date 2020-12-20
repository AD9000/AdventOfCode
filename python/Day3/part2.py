#!/usr/bin/env python3
from sys import stdin

grid = stdin.readlines()
rows = len(grid)
columns = len(grid[0]) - 1  # newline


def findSlope(right, down):
    col = right
    count = 0

    for i in range(down, rows, down):
        if grid[i][col] == "#":
            count += 1

        col = (col + right) % columns

    return count


ans = 1
moves = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
for move in moves:
    ans *= findSlope(*move)

print(ans)
