# 5567 : 결혼식
# https://www.acmicpc.net/problem/5567

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

visited =[-1 for _ in range(n+1)]
visited[1] = 0
queue = deque([1])

while queue:
    point = queue.popleft()

    for nex in graph[point]:
        if visited[nex] == -1:
            visited[nex] = visited[point] + 1
            queue.append(nex)

count = 0
for i in range(1, n+1):
    if 0 < visited[i] <= 2:
        count += 1

print(count)