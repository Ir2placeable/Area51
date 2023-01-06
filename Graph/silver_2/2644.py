# 2644 : 촌수 계산
# https://www.acmicpc.net/problem/2644
from collections import deque

n = int(input())
target1, target2 = map(lambda x: int(x), input().split(" "))
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)


visited = [0 for _ in range(n+1)]
visited[target1] = 1

queue = deque([target1])
while queue:
    start = queue.popleft()

    for end in graph[start]:
        if visited[end] == 0:
            visited[end] = visited[start] + 1
            queue.append(end)

if visited[target2] == 0:
    print(-1)
else:
    print(visited[target2] - 1)