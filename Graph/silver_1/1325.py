# 1325 : 효율적인 해킹
# https://www.acmicpc.net/problem/1325
from collections import deque

n, m = map(lambda x: int(x), input().split(" "))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[b].append(a)
# print(graph)

hacking = []
max_count = 0
for start in range(1, n+1):
    count = 0
    visited = [0 for _ in range(n+1)]
    visited[start] = 1

    queue = deque([start])
    while queue:
        count += 1
        point = queue.popleft()

        for next_point in graph[point]:
            if visited[next_point] == 0:
                visited[next_point] = 1
                queue.append(next_point)

    max_count = max(max_count, count)
    hacking.append([start, count])

result = []
for hack in hacking:
    if hack[1] == max_count:
        result.append(hack[0])
print(*result)