# 1로 만들기
# https://www.acmicpc.net/problem/1463

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
import sys

n = int(sys.stdin.readline())
dp = [0, 1, 1, 1, 2]

if n < len(dp):
    print(dp[n])
else:
    index = 5
    while index < n+1:
        temp = [dp[index-1] + 1]
        if index % 3 == 0:
            temp.append(dp[index//3] + 1)
        if index % 2 == 0:
            temp.append(dp[index//2] + 1)

        dp.append(min(temp))
        index += 1

    print(dp[n])