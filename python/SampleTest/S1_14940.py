# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = [[0 for _ in range(width)] for _ in range(height)]
visited = [[-1 for _ in range(width)] for _ in range(height)]

x, y = 0, 0
initialized = False
for i in range(height):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    for j in range(width):
        maps[i][j] = temp[j]
        if maps[i][j] == 0:
            visited[i][j] = 0
        if not initialized and maps[i][j] == 2:
            y = i
            x = j
            initialized = True

visited[y][x] = 0
queue = deque([[y, x]])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    qy, qx = queue.popleft()

    for i in range(4):
        ny = qy + dy[i]
        nx = qx + dx[i]

        if ny < 0 or nx < 0 or ny > height-1 or nx > width-1 or maps[ny][nx] == 0:
            continue

        if visited[ny][nx] == -1:
            visited[ny][nx] = visited[qy][qx] + 1
            queue.append([ny, nx])

for temp in visited:
    print(*temp)