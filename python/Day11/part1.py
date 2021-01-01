#!/usr/bin/env python3
from sys import stdin
from copy import deepcopy

grid = []
for line in stdin:
    grid.append(list(line.strip()))

l, w = len(grid), len(grid[0])
newGrid = [[None] * w for _ in range(l)]
moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
occupied = 0


def check(i, j):
    if grid[i][j] == ".":
        return False
    curr = grid[i][j] == "#"

    count = 0
    for (a, b) in moves:
        if i + a < 0 or i + a >= l:
            continue
        if j + b < 0 or j + b >= w:
            continue

        count += grid[i + a][j + b] == "#"

    return (curr and count >= 4) or ((not curr) and count == 0)


def flip(grid, newGrid):
    global occupied
    flipped = False
    for row in range(l):
        for col in range(w):
            if check(row, col):
                newGrid[row][col] = "#" if grid[row][col] == "L" else "L"
                flipped = True
            else:
                newGrid[row][col] = grid[row][col]
            # print(grid[row][col], newGrid[row][col])

            occupied += newGrid[row][col] == "#"
    return flipped


while flip(grid, newGrid):
    grid = deepcopy(newGrid)
    occupied = 0

print(occupied)
