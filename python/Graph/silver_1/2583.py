# 2583 : 영역 구하기
# https://www.acmicpc.net/problem/2583
from collections import deque

height, width, num_k = map(lambda x: int(x), input().split(" "))

graph = [[0 for i in range(width)] for j in range(height)]
for _ in range(num_k):
    x0, y0, x1, y1 = map(lambda x: int(x), input().split(" "))

    for y in range(y0, y1):
        for x in range(x0, x1):
            graph[y][x] = 1
# print(graph)

areas = []
for y in range(height):
    for x in range(width):
        if graph[y][x] == 0:
            area = 1
            graph[y][x] = 1

            # BFS 시작
            queue = deque([[y, x]])
            while queue:
                qy, qx = queue.popleft()

                for _x in range(max(0, qx-1), min(width, qx+2)):
                    if graph[qy][_x] == 0:
                        area += 1
                        graph[qy][_x] = 1
                        queue.append([qy, _x])
                for _y in range(max(0, qy-1), min(height, qy+2)):
                    if graph[_y][qx] == 0:
                        area += 1
                        graph[_y][qx] = 1
                        queue.append([_y, qx])

            areas.append(area)
areas.sort()
print(len(areas))
print(*areas)