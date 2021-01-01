#!/usr/bin/env python3
from sys import stdin

# possible bucket sort, but I'm lazy
nums = [0] + sorted([int(line.strip()) for line in stdin])
nums.append(nums[len(nums) - 1] + 3)

diff = [0] * 3
prev = None
for i in nums:
    if prev is not None:
        diff[i - prev - 1] += 1
    prev = i

print(diff[0] * diff[2])
