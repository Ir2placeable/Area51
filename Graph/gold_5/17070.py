# 17070 : 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070
import sys
from collections import deque

# 가로 : 0 / 새로 : 1 / 대각선 : 2
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
# print(graph)

queue = deque([[0, 1, 0]])
way_count = 0
while queue:
    y, x, direction = queue.popleft()
    if x == n-1 and y == n-1:
        way_count += 1
        continue

    # 파이프 형태가 가로일 때
    if direction == 0:
        if x + 1 < n and graph[y][x + 1] == 0:
            queue.append([y, x+1, 0])
        if x + 1 < n and y + 1 < n and graph[y + 1][x + 1] == 0 and graph[y + 1][x] == 0 and graph[y][x + 1] == 0:
            queue.append([y+1, x+1, 2])

    # 파이프 형태가 세로일 때
    elif direction == 1:
        if y + 1 < n and graph[y + 1][x] == 0:
            queue.append([y+1, x, 1])
        if x + 1 < n and y + 1 < n and graph[y + 1][x + 1] == 0 and graph[y + 1][x] == 0 and graph[y][x + 1] == 0:
            queue.append([y + 1, x + 1, 2])

    # 파이프 형태가 대각선일 때
    elif direction == 2:
        if x + 1 < n and graph[y][x + 1] == 0:
            queue.append([y, x+1, 0])
        if y + 1 < n and graph[y + 1][x] == 0:
            queue.append([y+1, x, 1])
        if x + 1 < n and y + 1 < n and graph[y + 1][x + 1] == 0 and graph[y + 1][x] == 0 and graph[y][x + 1] == 0:
            queue.append([y + 1, x + 1, 2])
print(way_count)