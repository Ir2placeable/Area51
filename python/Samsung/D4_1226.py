# BFS/DFS

# 14분 컷

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for test_case in range(1, 11):
    t = int(input())
    maps = []
    for _ in range(16):
        maps.append(list(input()))

    visited = [[0 for _ in range(16)] for _ in range(16)]
    visited[1][1] = 1
    queue = deque([[1, 1]])

    result = 0
    while queue:
        qx, qy = queue.popleft()

        if maps[qx][qy] == '3':
            result = 1
            a, b = qx, qy
            break

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx < 0 or ny < 0 or nx > 15 or ny > 15:
                continue

            temp = maps[nx][ny]
            if visited[nx][ny] == 1 or maps[nx][ny] == '1':
                continue

            visited[nx][ny] = 1
            queue.append([nx, ny])
    print("#%d %d" % (test_case, result))