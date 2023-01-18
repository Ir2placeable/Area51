# 14495 : 피보나치 비스무리한 수열
# https://www.acmicpc.net/problem/14495

dp = [0, 1, 1, 1, 2, 3, 4]
n = int(input())

if n < len(dp):
    print(dp[n])
else:
    while len(dp) <= n:
        dp.append(dp[len(dp)-1] +  dp[len(dp)-3])

    print(dp[n])