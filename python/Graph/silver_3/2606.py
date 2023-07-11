# 2606 : 바이러스
# https://www.acmicpc.net/problem/2606
import sys

computers = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[] for _ in range(computers+1)]
for _ in range(n):
    a, b = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (computers+1)
visited[1] = 1
q = [1]
while q:
    cur = q.pop(0)

    for nex in graph[cur]:
        if visited[nex] == 0:
            q.append(nex)
            visited[nex] = 1

print(sum(visited)-1)