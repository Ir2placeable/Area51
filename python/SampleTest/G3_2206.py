# https://www.acmicpc.net/problem/2206

# 최단 경로 찾기 -> BFS 문제
# 탈출 조건에 벽 하나까지 부술 수 있다는 조건 넣기
# 벽을 부술 경우, 최단 거리가 짧아지므로 크기 조건 추가하기

import sys
from collections import deque

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(list(sys.stdin.readline().rstrip()))

visited = [[[0 for _ in range(2)] for _ in range(width)] for _ in range(height)]
visited[0][0][0] = 1
queue = deque([[0, 0, 0]])
result = -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    qy, qx, broke = queue.popleft()

    if qy == height-1 and qx == width-1:
        result = visited[qy][qx][broke]
        break

    for i in range(4):
        ny = qy + dy[i]
        nx = qx + dx[i]

        if nx < 0 or ny < 0 or nx > width - 1 or ny > height - 1:
            continue

        # 벽을 부술 수 있음.
        if broke == 0 and maps[ny][nx] == '1':
            visited[ny][nx][1] = visited[qy][qx][0] + 1
            queue.append([ny, nx, 1])
        # 일반 조건
        elif maps[ny][nx] == '0' and visited[ny][nx][broke] == 0:
            visited[ny][nx][broke] = visited[qy][qx][broke] + 1
            queue.append([ny, nx, broke])

print(result)