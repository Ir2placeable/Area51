# 1389 : 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
from collections import deque

n, m = map(lambda x: int(x), input().split(" "))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

bacon_number = []
for vertex in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    visited[vertex] = 1

    queue = deque([vertex])
    while queue:
        start = queue.popleft()

        for end in graph[start]:
            if visited[end] == 0:
                queue.append(end)
                visited[end] = visited[start] + 1
    bacon_number.append([vertex, sum(visited)])
bacon_number = sorted(bacon_number, key=lambda x: x[1])
print(bacon_number[0][0])