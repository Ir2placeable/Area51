# 11726 : 2xn 타일링
# https://www.acmicpc.net/problem/11726

# 숫자 n을 1과 2로 채우는 방법을 찾는 문제와 동일하다.

import sys
n = int(sys.stdin.readline())

dp = [1 for _ in range(n+1)]
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])