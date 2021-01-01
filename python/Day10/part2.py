#!/usr/bin/env python3
from sys import stdin
from collections import defaultdict

# possible bucket sort, but I'm lazy
nums = sorted([int(line.strip()) for line in stdin])
l = len(nums)
nums.append(nums[l - 1] + 3)
l += 1

# dp[p] -> number of ways to arrange adapters < p to get p
# dp[p] = dp[p - 1] + dp[p - 2] + dp[p - 3]
# base case: dp[0] -> 1

dp = defaultdict(lambda: 0, {0: 1})

for i in nums:
    for j in range(1, 4):
        if (i - j) in dp:
            dp[i] += dp[i - j]

print(dp[nums[l - 1]])
