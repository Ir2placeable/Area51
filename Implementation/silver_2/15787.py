# https://www.acmicpc.net/problem/15787

import sys
from collections import deque

n, m = map(lambda x: int(x), sys.stdin.readline().split())
trains = [deque([0 for _ in range(20)]) for _ in range(n)]
for _ in range(m):
    operator = list(map(lambda x: int(x), sys.stdin.readline().split()))

    if operator[0] == 1:
        trains[operator[1] - 1][operator[2] - 1] = 1
    elif operator[0] == 2:
        trains[operator[1] - 1][operator[2] - 1] = 0
    elif operator[0] == 3:
        trains[operator[1] - 1].rotate(1)
        trains[operator[1] - 1][0] = 0
    elif operator[0] == 4:
        trains[operator[1] - 1].rotate(-1)
        trains[operator[1] - 1][-1] = 0

result = []
for train in trains:
    if train not in result:
        result.append(train)
print(len(result))