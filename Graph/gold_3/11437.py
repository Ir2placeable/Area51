# https://www.acmicpc.net/problem/11437

# DFS
import sys
sys.setrecursionlimit(10**5)


def DFS(cur_node, cur_depth):
    visited[cur_node] = True
    depth[cur_node] = cur_depth

    for next_node in graph[cur_node]:
        if visited[next_node]:
            continue
        parents[next_node] = cur_node
        DFS(next_node, cur_depth + 1)


def LCA(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parents[a]
        else:
            b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]

    return a


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

DFS(1, 0)
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    print(LCA(a, b))

# BFS
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# graph = [[] for _ in range(n + 1)]
# for _ in range(n-1):
#     a, b = map(lambda x: int(x), sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# m = int(sys.stdin.readline())
# targets = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(m)]
#
# # parent, depth
# nodes = [[0, 0, i] for i in range(n+1)]
# visited = [False for _ in range(n+1)]
# visited[1] = True
# queue = deque([[0, 1]])
#
# while queue:
#     depth, node = queue.popleft()
#
#     for next_node in graph[node]:
#         if visited[next_node]:
#             continue
#
#         visited[next_node] = True
#         nodes[next_node][0] = node
#         nodes[next_node][1] = depth + 1
#         queue.append([depth + 1, next_node])
#
# for a, b in targets:
#     nodeA = nodes[a]
#     nodeB = nodes[b]
#     while nodeA[1] > nodeB[1]:
#         nodeA = nodes[nodeA[0]]
#     while nodeA[1] < nodeB[1]:
#         nodeB = nodes[nodeB[0]]
#     while nodeA[2] != nodeB[2]:
#         nodeA = nodes[nodeA[0]]
#         nodeB = nodes[nodeB[0]]
#     print(nodeA[2])