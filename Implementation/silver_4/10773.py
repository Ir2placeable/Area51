# https://www.acmicpc.net/problem/10773

import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        nums.pop()
    else:
        nums.append(k)
print(sum(nums))