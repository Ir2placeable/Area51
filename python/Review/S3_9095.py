# 양의 정수 n을 1, 2, 3으로 표현하는 방법 찾기
# dp 문제이다 -> 하나씩 손으로 써보며 점화식을 찾는다. + 필요한 초기값은 어디까지 인지 확인하고 세팅한다

# n=1 : 1 : 1
# n=2 : 11 2 : 2
# n=3 : 111 12 21 3 : 4
# n=4 : 1111 112 121 211 13 31 22 : 7
# dp[k] = dp[k-1] + dp[k-2] + dp[k-3] / k >= 4

import sys

test_case = int(sys.stdin.readline())
for a in range(test_case):
    n = int(sys.stdin.readline())

    dp = [0 for _ in range(11)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])