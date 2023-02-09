# 다익스트라 알고리즘 문제이다.
# 맵의 크기는 최대 100 X 100 = 10000 이다.
# 18분 컷

import heapq

MAXSIZE = 10001
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

test_case = int(input())
for i in range(1, test_case + 1):
    n = int(input())
    maps = []
    for _ in range(n):
        maps.append(list(map(lambda x: int(x), list(input()))))

    total_cost = [[MAXSIZE for _ in range(n)] for _ in range(n)]
    total_cost[0][0] = 0
    queue = [[0, 0, 0]]

    while queue:
        # 현재 좌표와 현재까지의 비용
        cost, qx, qy = heapq.heappop(queue)

        # 목적지에 도착한 경우
        if qx == n - 1 and qy == n - 1:
            break

        for k in range(4):
            # 다음 이동할 좌표
            nx = qx + dx[k]
            ny = qy + dy[k]

            # 맵 밖을 벗어난 경우
            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue

            if total_cost[nx][ny] > cost + maps[nx][ny]:
                total_cost[nx][ny] = cost + maps[nx][ny]
                heapq.heappush(queue, [total_cost[nx][ny], nx, ny])

    result = total_cost[n - 1][n - 1]
    print("#%d %d" % (i, result))