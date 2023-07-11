# 정상 순서로 있는 streak 중 길이가 가장 긴 것을 구한다. -> k
# result = n - k

import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))