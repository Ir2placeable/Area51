# https://www.acmicpc.net/problem/1913

import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

maps = [[0 for _ in range(n)] for _ in range(n)]

min_x, max_x = 0, n-1
min_y, max_y = 0, n-1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

index = n ** 2
cur_x, cur_y, cur_d = 0, 0, 0
target_x, target_y = 0, 0

while index > 0:
    if index == target:
        target_x, target_y = cur_x, cur_y

    maps[cur_y][cur_x] = index
    index -= 1

    if cur_d == 0 and cur_y == max_y:
        cur_d = (cur_d + 1) % 4
        min_x += 1
    elif cur_d == 1 and cur_x == max_x:
        cur_d = (cur_d + 1) % 4
        max_y -= 1
    elif cur_d == 2 and cur_y == min_y:
        cur_d = (cur_d + 1) % 4
        max_x -= 1
    elif cur_d == 3 and cur_x == min_x:
        cur_d = (cur_d + 1) % 4
        min_y += 1

    cur_x = cur_x + dx[cur_d]
    cur_y = cur_y + dy[cur_d]

for temp in maps:
    print(*temp)
print(target_y+1, target_x+1)