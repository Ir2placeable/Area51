# 1388 : 바닥 장식
# https://www.acmicpc.net/problem/1388
import sys

def dfs(x,y):
    if graph[x][y] == '-':
        graph[x][y] = 1

        for _y in [1, -1]:
            next_y = y + _y
            if (0 < next_y < m) and graph[x][next_y] == '-':
                dfs(x, next_y)

    elif graph[x][y] == '|':
        graph[x][y] = 1

        for _x in [1, -1]:
            next_x = x + _x
            if (0 < next_x < n) and graph[next_x][y] == '|':
                dfs(next_x, y)


n, m = map(lambda x: int(x), sys.stdin.readline().split())
graph = []
for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)

woods = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] != 1:
            dfs(x,y)
            woods += 1

print(woods)