# https://www.acmicpc.net/problem/1748

# n의 최대 자리수를 구한 뒤, 자리수를 하나씩 낮춰가며 계산한다.

import sys
n = int(sys.stdin.readline())
if n < 10:
    print(n)
else:
    base = 1
    while n // 10 ** base > 0:
        base += 1
    base -= 1

    result = (n - 10 ** base + 1) * (base + 1)
    for i in range(0, base):
        result += 9 * (10 ** i) * (i + 1)
    print(result)