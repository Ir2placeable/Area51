# 브루트포스
# 25분 컷

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maps = []
    for _ in range(n):
        maps.append(list(map(lambda x: int(x), input().split())))

    result_list = []
    for x in range(n):
        for y in range(n):
            queue = deque([[x, y, 1]])

            max_count = 0
            while queue:
                qx, qy, count = queue.popleft()
                max_count = max(max_count, count)

                for i in range(4):
                    nx = qx + dx[i]
                    ny = qy + dy[i]

                    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                        continue

                    if maps[nx][ny] == maps[qx][qy] + 1:
                        queue.append([nx, ny, count+1])
                        break

            result_list.append([maps[x][y], max_count])
    max_room = sorted(result_list, key=lambda x: x[1], reverse=True)[0][1]
    result = sorted(list(filter(lambda x: x[1] == max_room, result_list)))[0]
    print("#%d %d %d" %(test_case, result[0], result[1]))