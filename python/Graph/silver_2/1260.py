# 1260 : DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
n, m, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for temp in graph:
    temp.sort()

# print(graph)

dfs_result = []
bfs_result = []


def dfs(start_point):
    if start_point not in dfs_result:
        dfs_result.append(start_point)

        for point in graph[start_point]:
            dfs(point)


def bfs(start_point):
    q = [start_point]

    while q:
        point = q.pop(0)
        if point not in bfs_result:
            bfs_result.append(point)

            for temp in graph[point]:
                q.append(temp)


dfs(k)
bfs(k)
result1 = ''
result2 = ''
for i in range(0, len(dfs_result)-1):
    result1 += str(dfs_result[i]) + " "
result1 += str(dfs_result[-1])

for i in range(0, len(bfs_result)-1):
    result2 += str(bfs_result[i]) + " "
result2 += str(bfs_result[-1])

print(result1)
print(result2)

