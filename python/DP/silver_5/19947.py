# 19947 : 투자의 귀재 배주형
# https://www.acmicpc.net/problem/19947

# 25542 10
h, y = map(lambda x: int(x), input().split())
dp = [0 for _ in range(y+1)]

dp[0] = h
for i in range(1, y+1):
    if i >= 5:
        dp[i] = max(dp[i-5] * 1.35, dp[i-3] * 1.2, dp[i-1] * 1.05)
    elif i >= 3:
        dp[i] = max(dp[i-3] * 1.2, dp[i-1] * 1.05)
    else:
        dp[i] = dp[i-1] * 1.05
    dp[i] = int(dp[i])

print(dp[y])