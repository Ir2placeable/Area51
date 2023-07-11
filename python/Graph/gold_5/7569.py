# 7569 : 토마토
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

a, b, c = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
graph = []
for i in range(c):
    temp = []
    for j in range(b):
        temp.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))
    graph.append(temp)

queue = deque([])
for z in range(c):
    for y in range(b):
        for x in range(a):
            if graph[z][y][x] == 1:
                queue.append([z, y, x])

visited = [[[0 for i in range(a)] for j in range(b)] for k in range(c)]
while queue:
    qz, qy, qx = queue.popleft()

    for _z in range(max(0, qz - 1), min(c, qz + 2)):
        if graph[_z][qy][qx] == 0:
            graph[_z][qy][qx] = 1
            visited[_z][qy][qx] = visited[qz][qy][qx] + 1
            queue.append([_z, qy, qx])
    for _y in range(max(0, qy - 1), min(b, qy + 2)):
        if graph[qz][_y][qx] == 0:
            graph[qz][_y][qx] = 1
            visited[qz][_y][qx] = visited[qz][qy][qx] + 1
            queue.append([qz, _y, qx])
    for _x in range(max(0, qx - 1), min(a, qx + 2)):
        if graph[qz][qy][_x] == 0:
            graph[qz][qy][_x] = 1
            visited[qz][qy][_x] = visited[qz][qy][qx] + 1
            queue.append([qz, qy, _x])

days = 0
ripen = True
for z in range(c):
    for y in range(b):
        for x in range(a):
            if graph[z][y][x] == 0:
                ripen = False
            days = max(days, visited[z][y][x])

if ripen:
    print(days)
else:
    print(-1)