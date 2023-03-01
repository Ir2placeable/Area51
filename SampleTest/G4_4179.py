# https://www.acmicpc.net/problem/4179

# 지훈이가 탈출할 수 있는 시간을 만듬
# 불이 확산하는 시간을 만듬
# 탈출구를 돌면서, 불보다 지훈이가 빨리 온 경우를 체크함

# 불이 여러 개일 수 있다

# 탈출구 체크 조건에 특이한 조건이 있을 수 있다.

import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(height)]

cur_x, cur_y = 0, 0
fires = []
for y in range(height):
    for x in range(width):
        if maps[y][x] == 'J':
            cur_y, cur_x = y, x
        if maps[y][x] == 'F':
            fires.append([y, x])

visited = [[0 for _ in range(width)] for _ in range(height)]
fire_spreading = [[0 for _ in range(width)] for _ in range(height)]
visited[cur_y][cur_x] = 1
for fire_y, fire_x in fires:
    fire_spreading[fire_y][fire_x] = 1

# 지훈이가 이동하는 시간값
queue = deque([[cur_y, cur_x]])
while queue:
    qy, qx = queue.popleft()

    for i in range(4):
        ny = qy + dy[i]
        nx = qx + dx[i]

        if ny < 0 or nx < 0 or ny > height - 1 or nx > width - 1 or maps[ny][nx] == '#':
            continue

        if visited[ny][nx] == 0:
            visited[ny][nx] = visited[qy][qx] + 1
            queue.append([ny, nx])

# 불이 이동하는 시간값
queue = deque(fires)
while queue:
    qy, qx = queue.popleft()

    for i in range(4):
        ny = qy + dy[i]
        nx = qx + dx[i]

        if ny < 0 or nx < 0 or ny > height - 1 or nx > width - 1 or maps[ny][nx] == '#':
            continue

        if fire_spreading[ny][nx] == 0:
            fire_spreading[ny][nx] = fire_spreading[qy][qx] + 1
            queue.append([ny, nx])

for temp in visited:
    print(*temp)
print()
for temp in fire_spreading:
    print(*temp)
# 탈출구를 돌면서 값이 있는지 확인한다. visited[y][x] < fire_spreading[y][x]
result = sys.maxsize
breakthroughs = [[i, 0] for i in range(height)] + [[i, width - 1] for i in range(height)] + [[0, i] for i in
                                                                                             range(width)] + [
                    [height - 1, i] for i in range(width)]

for y, x in breakthroughs:
    # 이동할 수 없는 곳
    if visited[y][x] == 0:
        continue

    # 불보다 빠르게 이동한 곳
    if fire_spreading[y][x] != 0 and visited[y][x] >= fire_spreading[y][x]:
        continue

    result = min(result, visited[y][x])

if result == sys.maxsize:
    result = 'IMPOSSIBLE'

print(result)