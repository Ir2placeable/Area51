# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

test_case = int(input())
dp = [1, 1, 2]
for _ in range(test_case):
    n = int(input())
    while len(dp) < n+1:
        dp.append(dp[len(dp)-2] + dp[len(dp)-1] + dp[len(dp)-3])

    print(dp[n])
