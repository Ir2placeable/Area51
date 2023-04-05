# https://www.acmicpc.net/problem/9461
import sys

test_case = int(sys.stdin.readline())

dp = [0, 1, 1, 1, 2, 2]
for _ in range(test_case):
    n = int(sys.stdin.readline())

    if n < 6:
        print(dp[n])
        continue

    for i in range()