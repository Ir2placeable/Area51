# 2178 : 미로 탐색
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

n, m = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

graph = []
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    temp_list = []
    for temp2 in temp:
        temp_list.append(int(temp2))
    graph.append(temp_list)
# print(graph)


visited = [[0 for i in range(m)] for _ in range(n)]
visited[0][0] = 1
# print(visited)

queue = deque([[0, 0]])
while queue:
    qy, qx = queue.popleft()

    for _x in range(max(0, qx-1), min(m, qx+2)):
        if graph[qy][_x] == 1 and visited[qy][_x] == 0:
            visited[qy][_x] = visited[qy][qx] + 1
            queue.append([qy, _x])
    for _y in range(max(0, qy-1), min(n, qy+2)):
        if graph[_y][qx] == 1 and visited[_y][qx] == 0:
            visited[_y][qx] = visited[qy][qx] + 1
            queue.append([_y, qx])

print(visited[-1][-1])