# https://www.acmicpc.net/problem/15989

# 딱 봐도 dp 문제임 -> 점화식을 찾는 것이 관건
import sys

dp = [0, 1]

index = 2
while index < 30:
    temp = dp[index-1]
    if index % 2 == 0:
        temp += 
    if index % 3 == 0:
        temp += 1
    dp.append(temp)
    index += 1
print(dp[4], dp[7], dp[10])