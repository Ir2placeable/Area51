# 9507 : Generations of Tribbles
# https://www.acmicpc.net/problem/9507
import sys

dp = [1, 1, 2, 4]

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())

    if n < len(dp)-1:
        print(dp[n])
    else:
        while len(dp)-1 < n:
            index = len(dp)
            dp.append(dp[index-1] + dp[index-2] + dp[index-3] + dp[index-4])

        print(dp[n])