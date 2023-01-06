# 11060 : 점프 점프
# https://www.acmicpc.net/problem/11060

n = int(input())
jumps = list(map(lambda x: int(x), input().split(" ")))

graph = [[] for _ in range(n)]
for i in range(0, n):
    for j in range(1, jumps[i]+1):
        if i + j >= n:
            continue
        graph[i].append(i+j)

# print(graph)

visited = [0 for _ in range(n)]
visited[0] = 1

from collections import deque
queue = deque([0])

while queue:
    start = queue.popleft()

    for nex in graph[start]:
        if visited[nex] == 0:
            visited[nex] = visited[start] + 1
            queue.append(nex)

print(visited[-1] - 1)
