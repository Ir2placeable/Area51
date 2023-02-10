# 구현

# 30분 초과 실패!

from collections import deque

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maps = []
    for _ in range(n):
        maps.append(list(input()))

    result = 0
    for y in range(n):
        for x in range(n):
            if maps[y][x] != '.':
                continue
            result += 1

            queue = deque([[y, x]])
            while queue:
                qy, qx = queue.popleft()

                mines = 0
                for i in range(8):
                    ny = qy + dy[i]
                    nx = qx + dx[i]

                    if ny < 0 or nx < 0 or ny > n-1 or nx > n-1:
                        continue

                    if maps[ny][nx] == '*':
                        mines += 1

                # 주변에 지뢰가 있는 경우
                if mines > 0:
                    maps[qy][qx] = mines
                    continue

                maps[qy][qx] = 0
                # 주변에 지뢰가 없는 경우 -> 연쇄작용!
                for i in range(8):
                    ny = qy + dy[i]
                    nx = qx + dx[i]

                    if ny < 0 or nx < 0 or ny > n - 1 or nx > n - 1:
                        continue

                    if maps[ny][nx] == '.':
                        queue.append([ny, nx])
    print(result)