# https://www.acmicpc.net/problem/1987

# BFS 알고리즘을 베이스로 한 문제이다.
# 통과조건에 이때까지 지나가지 않은 알파벳을 기준으로 한다. -> 알파벳은 26개로 고정되어 있으므로 미리 선언해서 사용한다.
# 26개를 일일히 적기는 귀찮으므로 defaultdict 를 사용한다.

# BFS인 줄 알았으나 DFS이다. -> 최대한 갈 수 있는 길 문제임
# 갔다가 조건에 맞지 않으면 돌아와야 하므로 -> 백트래킹이 추가된다.
# BFS + backtracking

import sys

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    temp = list(sys.stdin.readline().strip())
    temp2 = []
    for temp3 in temp:
        temp2.append(temp3)
    maps.append(temp2)
print(maps)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x, visited):
    global result
    result = max(result, len(visited))
    print(x, y, visited)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny > height-1 or nx > width-1:
            continue

        if maps[ny][nx] in visited:
            continue

        visited.append(maps[ny][nx])
        dfs(ny, nx, visited[:])


result = 0
temp = [maps[0][0]]
dfs(0, 0, temp)
print(result)