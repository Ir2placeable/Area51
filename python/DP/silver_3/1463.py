# 1로 만들기
# https://www.acmicpc.net/problem/1463

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[n])