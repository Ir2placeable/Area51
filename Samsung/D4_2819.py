# 브루트포스 + BFS/DFS 문제이다.
# 15분 컷

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for test_case in range(1, t+1):
    maps = []
    for _ in range(4):
        maps.append(list(input().split()))

    cases = set()
    for x in range(4):
        for y in range(4):

            # len, x, y, string
            queue = deque([[1, x, y, maps[x][y]]])

            while queue:
                index, qx, qy, string = queue.popleft()

                if index == 7:
                    cases.add(string)
                    continue

                for i in range(4):
                    nx = qx + dx[i]
                    ny = qy + dy[i]

                    if nx < 0 or ny < 0 or nx > 3 or ny > 3:
                        continue

                    queue.append([index+1, nx, ny, string+maps[nx][ny]])
    result = len(cases)
    print("#%d %d" % (test_case, result))