# 2667 : 단지번호붙이기
# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    temp_list = []
    for temp2 in temp:
        temp_list.append(int(temp2))
    graph.append(temp_list)

visited = [[0 for i in range(n)] for j in range(n)]

department = []
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            count = 1
            graph[y][x] = 0

            # BFS
            queue = deque([[y, x]])
            while queue:
                qy, qx = queue.popleft()

                for _y in range(max(0, qy-1), min(n, qy+2)):
                    if graph[_y][qx] == 1:
                        count += 1
                        graph[_y][qx] = 0
                        queue.append([_y, qx])

                for _x in range(max(0, qx-1), min(n, qx+2)):
                    if graph[qy][_x] == 1:
                        count += 1
                        graph[qy][_x] = 0
                        queue.append([qy, _x])

            department.append(count)

print(len(department))
department.sort()
for num in department:
    print(num)