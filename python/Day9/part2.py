#!/usr/bin/env python3
from sys import stdin
from collections import deque, defaultdict

sums = defaultdict(lambda: 0)
# preamble
nums = deque([int(input()) for i in range(25)])
allNums = list(nums)

l = len(nums)

for i in range(l):
    for j in range(i + 1, l):
        sums[nums[i] + nums[j]] += 1

weak = -1
for i in stdin:
    i = int(i)
    allNums.append(i)
    # check i
    if sums[i] == 0:
        weak = i
        break
    else:
        lastNum = nums.popleft()
        for j in nums:
            sums[lastNum + j] -= 1
            if sums[lastNum + j] == 0:
                sums.pop(lastNum + j)
            sums[i + j] += 1

        nums.append(i)


# contiguous sum -> sliding window
lowest = 0
s = allNums[lowest]
highest = 1
l = len(allNums)
while highest < l:
    print(s, weak, allNums[lowest], allNums[highest])
    if s == weak:
        print("done")
        break
    elif s > weak:
        s -= allNums[lowest]
        lowest += 1
    else:
        s += allNums[highest]
        highest += 1

# add check if last number was ever included

# print(len(allNums))
# print(allNums[lowest], allNums[highest - 1])

print(lowest, highest)
mn, mx = allNums[l - 1], 0
for i in range(lowest, highest):
    mn, mx = min(mn, allNums[i]), max(mx, allNums[i])


print(mn, mx, mn + mx)
