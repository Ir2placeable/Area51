# 13699 : 점화식
# https://www.acmicpc.net/problem/13699

# t(0)=1
# t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)

dp = [1, 1, 2]

while len(dp) < 37:
    value = 0
    for i in range(len(dp)):
        value += dp[i] * dp[len(dp)-1-i]
    dp.append(value)

print(dp[int(input())])