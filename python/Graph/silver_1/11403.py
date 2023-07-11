# 11403 : 경로 찾기
# https://www.acmicpc.net/problem/11403
from collections import deque
import sys

n = int(sys.stdin.readline())

graph = []
result = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    graph.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))

# 모든 점 마다 BFS 진행
for vertex in range(n):
    visiting = [0 for _ in range(n)]

    queue = deque()
    queue.append(vertex)
    while queue:
        start = queue.popleft()

        for i in range(n):
            if graph[start][i] == 1 and visiting[i] == 0:
                result[vertex][i] = 1
                queue.append(i)
                visiting[i] = 1

for i in result:
    print(*i)