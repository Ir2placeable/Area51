# 11724 : 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
from collections import deque

n, m = map(lambda x: int(x), input().split(" "))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
def bfs(point):
    queue = deque([point])
    visited[point] = 1

    while queue:
        vertex = queue.popleft()

        for next_point in graph[vertex]:
            if visited[next_point] == 0:
                queue.append(next_point)
                visited[next_point] = 1


connected = 0
for start_point in range(1, n+1):
    if visited[start_point] == 0:
        connected += 1
        bfs(start_point)

print(connected)
