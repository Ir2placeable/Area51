# https://www.acmicpc.net/problem/2579

# 한눈에 보아도 DP 문제이다. -> DP 문제는 점화식을 구하는 것이 관건이다.
# 직전 계단을 밟았을 때 경우 / 직전 계단을 밟지 않았을 때 경우 로 분리한다.

import sys
n = int(sys.stdin.readline())
nums = [0 for _ in range(301)]
for i in range(n):
    nums[i] = int(sys.stdin.readline())

dp = [0 for _ in range(301)]
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]
dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])

for i in range(3, n):
    dp[i] = nums[i] + max(dp[i-3] + nums[i-1], dp[i-2])
print(dp[n-1])