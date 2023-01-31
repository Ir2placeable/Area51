# https://www.acmicpc.net/problem/1193

import sys
n = int(sys.stdin.readline())

# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 4

line = 1
while n > line:
    n -= line
    line += 1

# 홀수 라인은 오름차순
# 짝수 라인은 내림차순
if line % 2 == 1:
    a, b = line, 1
    for _ in range(1, n):
        a -= 1
        b += 1
else:
    a, b = 1, line
    for _ in range(1, n):
        a += 1
        b -= 1

print(str(a) + '/' + str(b))