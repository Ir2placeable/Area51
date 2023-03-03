# https://www.acmicpc.net/problem/15989

import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())

    dp = [0 for i in range(n+1)]
    for i in range(1, n+1):
        dp[i] = dp[i-1]