#!/usr/bin/env python3
from sys import stdin
from collections import deque, defaultdict

sums = defaultdict(lambda: 0)
# preamble
nums = deque([int(input()) for i in range(25)])

l = len(nums)

for i in range(l):
    for j in range(i + 1, l):
        sums[nums[i] + nums[j]] += 1

weak = -1
for i in stdin:
    i = int(i)
    # check i
    if sums[i] == 0:
        weak = i
        break
    else:
        lastNum = nums.popleft()
        for j in nums:
            prev = lastNum + j
            sums[prev] -= 1
            if sums[prev] == 0:
                sums.pop(prev)

            sums[i + j] += 1

print(weak)
