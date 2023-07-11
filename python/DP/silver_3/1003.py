# 1003 : 피보나치 함수
# https://www.acmicpc.net/problem/1003

import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())

    dp = [[0 for _ in range(2)] for _ in range(max(n+1, 3))]
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    dp[2] = [1, 1]

    for i in range(3, n+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

    print(*dp[n])