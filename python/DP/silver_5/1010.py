# 1010 : 다리놓기
# https://www.acmicpc.net/problem/1010
import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    if a < b :
        a, b = b, a

    up = 1
    for i in range(b):
        up *= a
        a -= 1

    down = 1
    for i in range(1, b+1):
        down *= i

    print(up // down)