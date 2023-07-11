# 18352 : 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

n, m, k, start = map(lambda x: int(x), input().split(" "))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
# print(graph)

visited = [0 for _ in range(n+1)]
visited[start] = 1

from collections import deque

queue = deque([start])
while queue:
    point = queue.popleft()

    for nex in graph[point]:
        if visited[nex] == 0:
            visited[nex] = visited[point] + 1
            queue.append(nex)

flag = True
for i in range(1, n+1):
    if visited[i] == k+1:
        flag = False
        print(i)

if flag:
    print(-1)