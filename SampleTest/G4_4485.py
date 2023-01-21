# https://www.acmicpc.net/problem/4485

# 길 찾기 + 비용 최소 -> 다익스트라 알고리즘 -> heapq 사용 -> 시간초과 발생
# 다익스트라 알고리즘을 함수로 정의해보자..

import sys, heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
test_case = 0

while True:
    test_case += 1

    n = int(sys.stdin.readline())
    if n == 0:
        break
    maps = []
    for _ in range(n):
        maps.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

    cost = [[sys.maxsize for i in range(n)] for j in range(n)]
    cost[0][0] = maps[0][0]
    queue = [[cost[0][0], 0, 0]]

    while queue:
        qcost, qx, qy = heapq.heappop(queue)

        if qx == n-1 and qy == n-1:
            break

        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                next_cost = qcost + maps[nx][ny]

                if next_cost < cost[nx][ny]:
                    cost[nx][ny] = next_cost
                    heapq.heappush(queue, [next_cost, nx, ny])

    print(f'Problem {test_case}: {cost[n-1][n-1]}')