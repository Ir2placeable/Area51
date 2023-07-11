# 2468 : 안전 영역
# https://www.acmicpc.net/problem/2468
from copy import deepcopy

n = int(input())
graph = []
max_height = 0
for _ in range(n):
    temp = list(map(lambda x: int(x), input().split(" ")))
    max_height = max(max_height, max(temp))
    graph.append(temp)
# print(max_height)
# print(graph)

max_lands = -1
for height in range(max_height, -1, -1):
    # 그래프 재생성하기
    target_graph = deepcopy(graph)
    for y in range(n):
        for x in range(n):
            if target_graph[y][x] > height:
                target_graph[y][x] = 1
            else:
                target_graph[y][x] = 0
    # print(height)
    # print(target_graph)

    from collections import deque

    land = 0
    for y in range(n):
        for x in range(n):
            if target_graph[y][x] == 1:
                land += 1

                # BFS start
                queue = deque([[y, x]])
                target_graph[y][x] = 0

                while queue:
                    qy, qx = queue.popleft()

                    for _y in range(max(0, qy-1), min(n, qy+2)):
                        if target_graph[_y][qx] == 1:
                            target_graph[_y][qx] = 0
                            queue.append([_y, qx])

                    for _x in range(max(0, qx-1), min(n, qx+2)):
                        if target_graph[qy][_x] == 1:
                            target_graph[qy][_x] = 0
                            queue.append([qy, _x])

    max_lands = max(max_lands, land)
print(max_lands)