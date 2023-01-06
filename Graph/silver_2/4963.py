# 4963 : 섬의 개수
# https://www.acmicpc.net/problem/4963
from collections import deque

# 단순한 BFS 문제죠?
while True:
    # a : 가로 / b : 세로
    a, b = map(lambda x: int(x), input().split(" "))
    if a + b == 0:
        break

    graph = []
    for i in range(b):
        temp = list(map(lambda x: int(x), input().split(" ")))
        graph.append(temp)
    # print(graph)

    islands = 0
    for y in range(b):
        for x in range(a):
            if graph[y][x] == 1:
                islands += 1
                graph[y][x] = 0

                # BFS function
                queue = [[y, x]]
                while queue:
                    qy, qx = queue.pop(0)

                    for _y in range(max(0, qy-1), min(b, qy+2)):
                        for _x in range(max(0, qx-1), min(a, qx+2)):
                            if graph[_y][_x] == 1:
                                queue.append([_y, _x])
                                graph[_y][_x] = 0

    print(islands)
