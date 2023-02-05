# https://www.acmicpc.net/problem/2466

# 참외밭의 모양이 정해져 있다.
# 큰 사각형에서 작은 사각형을 뺴면 되는 문제이다.

# 1 : 동
# 2 : 서
# 3 : 남
# 4 : 북

import sys

k = int(sys.stdin.readline())
cases = []
for _ in range(6):
    cases.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

max_x, max_y = 0, 0
for direction, scala in cases:
    if direction == 1 or direction == 2:
        max_x = max(max_x, scala)
    elif direction == 3 or direction == 4:
        max_y = max(max_y, scala)

min_x, min_y = 0, 0
for i in range(6):
    direction, scala = cases[i]
    if (direction == 1 or direction == 2) and scala == max_x and min_y == 0:
        min_y = abs(cases[(i+1)%6][1] - cases[(i-1)%6][1])

    elif (direction == 3 or direction == 4) and scala == max_y and min_x == 0:
        min_x = abs(cases[(i+1)%6][1] - cases[(i-1)%6][1])

print(k * (max_x * max_y - min_x * min_y))