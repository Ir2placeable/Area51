# 9625 : BABBA
# https://www.acmicpc.net/problem/9625

import sys
k = int(sys.stdin.readline())

a, b = 1, 0

while k > 0:
    a, b = b, a+b
    k -= 1
print(a, b)