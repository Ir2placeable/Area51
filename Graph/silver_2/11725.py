# 11725 : 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())

graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(lambda x: int(x), input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

parents = [0 for i in range(n+1)]


def dfs(vertex):
    for next_vertex in graph[vertex]:
        if parents[next_vertex] == 0:
            parents[next_vertex] = vertex
            dfs(next_vertex)


dfs(1)
for i in range(2, n+1):
    print(parents[i])