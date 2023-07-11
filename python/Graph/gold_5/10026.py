# 10026 : 적록색약
# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    temp = []
    for char in string:
        temp.append(char)
    graph.append(temp)
# print(graph)

# normal
visited1 = [[0 for i in range(n)] for j in range(n)]
department1 = 0
for x in range(n):
    for y in range(n):
        if visited1[x][y] == 0:
            visited1[x][y] = 1
            department1 += 1

            queue1 = deque([[x, y]])
            while queue1:
                qx, qy = queue1.popleft()

                for _x in range(max(0, qx-1), min(n, qx+2)):
                    if graph[_x][qy] == graph[qx][qy] and visited1[_x][qy] == 0:
                        visited1[_x][qy] = 1
                        queue1.append([_x, qy])
                for _y in range(max(0, qy-1), min(n, qy+2)):
                    if graph[qx][_y] == graph[qx][qy] and visited1[qx][_y] == 0:
                        visited1[qx][_y] = 1
                        queue1.append([qx, _y])
print(department1)

# abnormal
visited2 = [[0 for i in range(n)] for j in range(n)]
department2 = 0
for x in range(n):
    for y in range(n):
        if visited2[x][y] == 0:
            visited2[x][y] = 1
            department2 += 1

            queue2 = deque([[x, y]])
            while queue2:
                qx, qy = queue2.popleft()

                for _x in range(max(0, qx-1), min(n, qx+2)):
                    if graph[qx][qy] == 'R' or graph[qx][qy] == 'G':
                        if (graph[_x][qy] == 'R' or graph[_x][qy] == 'G') and visited2[_x][qy] == 0:
                            visited2[_x][qy] = 1
                            queue2.append([_x, qy])
                    else:
                        if graph[_x][qy] == graph[qx][qy] and visited2[_x][qy] == 0:
                            visited2[_x][qy] = 1
                            queue2.append([_x, qy])
                for _y in range(max(0, qy-1), min(n, qy+2)):
                    if graph[qx][qy] == 'R' or graph[qx][qy] == 'G':
                        if (graph[qx][_y] == 'R' or graph[qx][_y] == 'G') and visited2[qx][_y] == 0:
                            visited2[qx][_y] = 1
                            queue2.append([qx, _y])
                    else:
                        if graph[qx][_y] == graph[qx][qy] and visited2[qx][_y] == 0:
                            visited2[qx][_y] = 1
                            queue2.append([qx, _y])
print(department2)