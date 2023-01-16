# 9625 : BABBA
# https://www.acmicpc.net/problem/9625

import sys
k = int(sys.stdin.readline())

result = [[1, 0], [0, 1]]

def dp(num):
    if num < 2:
        return result[num]

    return [dp(num-1)[1], dp(num-1)[0] + dp(num-1)[1]]

print(*dp(k))