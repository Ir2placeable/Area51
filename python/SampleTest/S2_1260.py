# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

n, m, start = map(lambda x: int(x), sys.stdin.readline().split())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    maps[a].append(b)
    maps[b].append(a)

for i in range(len(maps)):
    maps[i] = sorted(maps[i])
# print(maps)


def dfs(x, visited):
    result_dfs.append(x)

    for y in maps[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y, visited)


def bfs(x, visited):
    queue = deque([x])
    while queue:
        q = queue.popleft()
        result_bfs.append(q)

        for y in maps[q]:
            if not visited[y]:
                visited[y] = True
                queue.append(y)


temp = [False for _ in range(n+1)]
temp[start] = True

result_dfs = []
result_bfs = []
dfs(start, temp[:])
bfs(start, temp[:])
print(*result_dfs)
print(*result_bfs)