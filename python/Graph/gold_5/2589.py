# 2589 : 보물섬
# https://www.acmicpc.net/problem/2589
import sys
from collections import deque

height, width = map(lambda x: int(x), sys.stdin.readline().split())
graph = []
for _ in range(height):
    graph.append(list(sys.stdin.readline().strip()))
# print(graph)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(a, b):
    distance = 0
    visited = [[0 for i in range(width)] for j in range(height)]
    visited[a][b] = 1

    queue = deque([[a, b]])
    while queue:
        qy, qx = queue.popleft()

        for i in range(4):
            # 다음점
            ny, nx = qy + dy[i], qx + dx[i]
            # 탈출 조건
            if ny < 0 or ny > height - 1 or nx < 0 or nx > width - 1 or graph[ny][nx] == 'W':
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[qy][qx] + 1
                distance = max(distance, visited[ny][nx])
                queue.append([ny, nx])
    return distance - 1


max_distance = 0
for y in range(height):
    for x in range(width):
        if graph[y][x] == 'L':
            max_distance = max(max_distance, bfs(y, x))

print(max_distance)