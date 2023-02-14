# BFS
# 맵 만드는 과정이 핵심이다.

from collections import deque

dx = [-1, 0, -1, 1, 0, 1]
dy = [-1, -1, 0, 0, 1, 1]

t = int(input())
for test_case in range(1, t+1):
    a, b = map(lambda x: int(x), input().split())
    c = max(a, b)

    criteria, add = 0, 1
    while criteria < c:
        criteria += add
        add += 1

    n = add - 1
    maps = [[0 for _ in range(n)] for _ in range(n)]
    index = 1

    start_x, start_y = 0, 0
    target_x, target_y = 0, 0
    for i in range(n):
        for j in range(i+1):
            maps[i][j] = index
            if index == a:
                start_x, start_y = j, i
            if index == b:
                target_x, target_y = j, i
            index += 1

    # print(start_y, start_x)
    # print(target_y, target_x)
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[start_y][start_x] = 0
    queue = deque([[start_y, start_x]])

    result = 0
    while queue:
        qy, qx = queue.popleft()
        if qy == target_y and qx == target_x:
            result = visited[qy][qx]
            break

        for i in range(6):
            ny = qy + dy[i]
            nx = qx + dx[i]

            if ny < 0 or nx < 0 or ny > n-1 or nx > n-1 or maps[ny][nx] == 0:
                continue

            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[qy][qx] + 1
                queue.append([ny, nx])

    print("#%d %d" % (test_case, result))