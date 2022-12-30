# 16173 : 점프왕 쩰리 (Small)
# https://www.acmicpc.net/problem/16173

import sys

n = int(sys.stdin.readline())
graph = []
visited = []
for _ in range(n):
    graph.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
    visited.append([0] * n)
flag = False

q = [[0, 0]]
reached = False
while q:
    x, y = q.pop(0)

    if x >= n or y >= n:
        continue

    if graph[x][y] == -1:
        reached = True
        break

    if visited[x][y] == 0:
        visited[x][y] = 1
        step = graph[x][y]
        q.append([x+step, y])
        q.append([x, y+step])


if reached:
    print("HaruHaru")
else:
    print("Hing")