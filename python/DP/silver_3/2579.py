# 2579 : 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
n = int(sys.stdin.readline())
stairs = [0]
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

dp = [0 for _ in range(n+1)]
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    dp[i] = max(
        dp[i-3] + stairs[i-2] + stairs[i],
        dp[i-3] + stairs[i-1] + stairs[i],
        dp[i-4] + stairs[i-2] + stairs[i]
    )
print(dp)