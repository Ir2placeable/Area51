# https://www.acmicpc.net/problem/11438
import sys


def getParent(cur_node, cur_depth):
    depth[cur_node] = cur_depth
    visited[cur_node] = True

    for next_node in graph[cur_node]:
        if visited[next_node]:
            continue
        parents[next_node][0] = cur_node
        getParent(next_node, cur_depth + 1)


def getAncestors():
    # i : 2**i 번째 부모의 인덱스
    for i in range(1, 21):
        # j : node의 index
        for j in range(1, n+1):
            # parents[j][i] : j번째 node의 2**i번째 부모의 값
            parents[j][i] = parents[parents[j][i-1]][i-1]


def LCA(a, b):


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

parents = [[0 for _ in range(21)] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

getParent(1, 0)
getAncestors()

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(lambda x: int(x), sys.stdin.readline().split())
    print(LCA(a, b))