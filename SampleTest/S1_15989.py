# https://www.acmicpc.net/problem/15989

# 딱 봐도 dp 문제임 -> 점화식을 찾는 것이 관건
import sys

# 0 : 1
# 1 : 1
# 2 : 1 / 2
# 3 : 1 / 2 / 3
# 4 : 1 / 2 / 3 / 22
# 5 : 1 / 2 / 3 / 22 / 23
# 6 : 1 / 2 / 3 / 22 / 23 / 33 / 222


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n = int(sys.stdin.readline())

    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        if i % 2 == 0:
            dp[i] += dp[i-2]
        if i % 3 == 0:
            dp[i] += dp[i-3]


    print(dp)
    print(dp[n])