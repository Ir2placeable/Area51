# 7576 : 토마토
# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

width, height = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
graph = []
for _ in range(height):
    graph.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))
# print(graph)

queue = deque([])
for y in range(height):
    for x in range(width):
        if graph[y][x] == 1:
            queue.append([y, x])

visited = [[0 for i in range(width)] for j in range(height)]
while queue:
    qy, qx = queue.popleft()

    for _y in range(max(0, qy-1), min(height, qy+2)):
        if graph[_y][qx] == 0:
            graph[_y][qx] = 1
            visited[_y][qx] = visited[qy][qx] + 1
            queue.append([_y, qx])
    for _x in range(max(0, qx-1), min(width, qx+2)):
        if graph[qy][_x] == 0:
            graph[qy][_x] = 1
            visited[qy][_x] = visited[qy][qx] + 1
            queue.append([qy, _x])

days = 0
ripen = True
for y in range(height):
    for x in range(width):
        if graph[y][x] == 0:
            ripen = False
        days = max(days, visited[y][x])

if ripen:
    print(days)
else:
    print(-1)